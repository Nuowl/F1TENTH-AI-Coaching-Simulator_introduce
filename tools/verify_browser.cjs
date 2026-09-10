/* Browser verification. npm install && npx playwright install chromium first,
 * or point PLAYWRIGHT_MODULE / CHROMIUM_PATH to an existing installation. */
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const http = require('node:http');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '..');
const reportDir = path.join(root, 'docs', 'verification');
fs.mkdirSync(reportDir, {recursive: true});
const mime = {'.html':'text/html; charset=utf-8','.css':'text/css','.js':'text/javascript','.png':'image/png','.gif':'image/gif','.svg':'image/svg+xml','.md':'text/plain; charset=utf-8'};
const server = http.createServer((req,res) => {
  const pathname = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
  if (!pathname.startsWith('/research-preview/')) {res.writeHead(404); return res.end();}
  let file = path.resolve(root, pathname.slice('/research-preview/'.length) || 'index.html');
  if (!file.startsWith(root + path.sep) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {res.writeHead(404);return res.end();}
  res.setHeader('Content-Type', path.extname(file) === '.mp4' ? 'video/mp4' : mime[path.extname(file)] || 'application/octet-stream');
  fs.createReadStream(file).pipe(res);
});
(async()=>{
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=`http://127.0.0.1:${server.address().port}/research-preview/`;
  const browser=await chromium.launch({headless:true, executablePath:process.env.CHROMIUM_PATH || undefined, args:['--no-sandbox']});
  const context=await browser.newContext({viewport:{width:1440,height:1050},reducedMotion:'reduce'});
  const page=await context.newPage();
  const errors=[]; const failures=[]; const gifs=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('response',r=>{if(r.status()>=400) failures.push(r.url());});
  page.on('request',r=>{if(r.url().endsWith('.mp4'))gifs.push(r.url());});
  const pages=fs.readdirSync(root).filter(p=>p.endsWith('.html')).sort();
  const results=[];
  for(const name of pages){
    await page.goto(base+name+'?lang=en');
    await page.locator('main').waitFor();
    await page.locator('video').evaluateAll(videos => Promise.all(videos.map(video => new Promise((resolve, reject) => {
      if (video.readyState >= 2) return resolve();
      video.addEventListener('loadeddata', resolve, {once:true});
      video.addEventListener('error', () => reject(new Error('Video decode failed: ' + video.src)), {once:true});
      setTimeout(() => reject(new Error('Video load timeout: ' + video.src)), 15000);
    }))));
    assert.equal(await page.locator('video').evaluateAll(videos => videos.every(v => v.videoWidth >= 1000 && v.muted && v.loop)), true);
    // Full-page captures must include below-fold lazy images as well.
    await page.locator('img[src]').evaluateAll(async images => {
      images.forEach(i => { i.loading = 'eager'; });
      await Promise.all(images.map(i => i.decode()));
    });
    const headings=await page.locator('[data-heading]').allTextContents();
    assert.equal(await page.locator('.side-link[aria-current="page"]').count(),1);
    for(const lang of ['en','ko']){
      await page.locator(`[data-language="${lang}"]`).click();
      assert.equal(await page.locator('html').getAttribute('lang'),lang);
      assert.deepEqual(await page.locator('[data-heading]').allTextContents(),headings);
      assert.equal(await page.locator(`[data-lang="${lang==='en'?'ko':'en'}"]:visible`).count(),0);
      for(const width of [360,390,768,1280,1440]){
        await page.setViewportSize({width,height:1000});
        assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),true,`${name} ${lang} ${width} overflow`);
      }
      await page.screenshot({path:path.join(reportDir,name.replace('.html',`-${lang}.png`)),fullPage:true});
      results.push({page:name,language:lang,widths:[360,390,768,1280,1440],status:'pass'});
    }
    const broken=await page.locator('img[src]').evaluateAll(images=>images.filter(i=>i.complete&&i.naturalWidth===0).map(i=>i.src));
    assert.deepEqual(broken,[]);
    assert.equal(await page.locator('figure:not([data-demo]) .media-tools').count(),0);
    assert.equal(await page.locator('figure[data-demo] .media-tools button').count(),2*await page.locator('figure[data-demo]').count());
    assert.equal(await page.locator('.media-tools').evaluateAll(nodes=>nodes.every(n=>!n.textContent.trim())),true);
  }
  assert.ok(gifs.length>0,'Original MP4s load');
  await page.goto(base+'index.html?lang=ko');
  assert.equal(await page.locator('[data-play]').first().getAttribute('aria-pressed'),'true');
  assert.equal(await page.locator('[data-play]').first().getAttribute('aria-label'),'정지');
  assert.equal(await page.locator('[data-icon-stop]').first().isVisible(),true);
  await page.locator('[data-play]').first().click();
  assert.equal(await page.locator('[data-play]').first().getAttribute('aria-pressed'),'false');
  assert.equal(await page.locator('figure video').first().evaluate(v => v.paused),true);
  assert.equal(await page.locator('[data-play]').first().getAttribute('aria-label'),'재생');
  assert.equal(await page.locator('[data-icon-play]').first().isVisible(),true);
  assert.equal(await page.locator('[data-icon-stop]').first().isVisible(),false);
  await page.locator('[data-play]').first().click();
  assert.equal(await page.locator('[data-play]').first().getAttribute('aria-pressed'),'true');
  await page.locator('[data-enlarge]').first().click();
  assert.equal(await page.locator('dialog').evaluate(d=>d.open),true);
  assert.match(await page.locator('dialog video').getAttribute('src'),/\.mp4$/);
  await page.waitForFunction(() => { const v = document.querySelector('dialog video'); return !v.paused && v.currentTime > 0; });
  await page.locator('dialog [data-play]').click();
  assert.equal(await page.locator('dialog video').evaluate(v=>v.paused),true);
  await page.keyboard.press('Escape');
  assert.equal(await page.locator('dialog').evaluate(d=>d.open),false);
  assert.equal(await page.locator('figure video').first().evaluate(v=>v.paused),true);
  await page.locator('.side-link[href^="replay.html"]').click();
  assert.equal(await page.locator('html').getAttribute('lang'),'ko');
  await page.goBack();
  assert.match(page.url(),/index.html/);
  await page.setViewportSize({width:390,height:844});
  await page.goto(base+'index.html?lang=ko');
  assert.equal(await page.locator('.js-nav').isVisible(),false);
  await page.locator('.mobile-menu').click();
  assert.equal(await page.locator('.js-nav').isVisible(),true);
  await page.locator('.mobile-menu').click();
  await page.screenshot({path:path.join(reportDir,'mobile-ko.png'),fullPage:true});
  await page.setViewportSize({width:1440,height:1050});
  await page.goto(base+'index.html?lang=en&embed=1');
  assert.equal(await page.locator('.masthead').isVisible(),false);
  await page.locator('.side-link[href^="replay.html"]').click();
  assert.match(page.url(),/embed=1/);
  await page.goto('file://'+path.join(root,'index.html')+'?lang=ko');
  assert.equal(await page.locator('html').getAttribute('lang'),'ko');
  await page.locator('.side-link[href^="replay.html"]').click();
  assert.equal(await page.locator('h2').textContent(),'Replay Studio');
  const nojs=await browser.newContext({javaScriptEnabled:false,viewport:{width:390,height:844}});
  const nj=await nojs.newPage(); await nj.goto(base+'index.html');
  assert.equal(await nj.locator('.js-nav').isVisible(),true);
  assert.equal(await nj.locator('main h2').textContent(),'Research Overview');
  await nojs.close();
  await page.goto(base+'index.html?lang=en');
  await page.evaluate(()=>document.body.style.zoom='2');
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),true);
  await page.screenshot({path:path.join(reportDir,'zoom-200.png'),fullPage:true});
  assert.deepEqual(errors,[]);assert.deepEqual(failures,[]);
  await page.goto(base+'background.html?lang=ko');
  for (const [heading, file] of [['2. How Learning to Coach Works','background-mechanism-ko.png'],['3. What the Paper Evaluated','background-study-ko.png'],['4. Why AutoDRIVE?','background-platform-ko.png']]) {
    await page.locator('h3').filter({hasText:heading}).evaluate(node => node.scrollIntoView({block:'start'}));
    await page.screenshot({path:path.join(reportDir,file)});
  }
  await page.locator('.platform-diagram img').evaluate(async img => { img.loading = 'eager'; await img.decode(); });
  await page.locator('.platform-diagram').screenshot({path:path.join(reportDir,'autodrive-architecture-ko.png')});
  await page.goto(base+'dashboard.html?lang=ko');
  assert.equal(await page.locator('.annotation-pin').count(),11);
  await page.locator('#dashboard-pin-2').click();
  assert.match(page.url(),/#dashboard-note-2$/);
  await page.locator('#dashboard-note-2 h4 a').click();
  assert.match(page.url(),/#dashboard-pin-2$/);
  await page.locator('.annotated-frame').first().screenshot({path:path.join(reportDir,'dashboard-annotations-ko.png')});
  await page.locator('.annotated-frame').last().screenshot({path:path.join(reportDir,'overlay-annotations-ko.png')});
  await page.setViewportSize({width:390,height:844});
  await page.locator('#overlay-note-2').evaluate(node=>node.scrollIntoView({block:'start'}));
  await page.screenshot({path:path.join(reportDir,'annotation-notes-mobile-ko.png')});
  await page.goto(base+'simulator.html?lang=ko');
  await page.locator('.device-grid').screenshot({path:path.join(reportDir,'input-devices-mobile-ko.png')});
  assert.deepEqual(errors,[]); assert.deepEqual(failures,[]);
  fs.writeFileSync(path.join(reportDir,'results.json'),JSON.stringify({results,errors,failures,checks:['language','invariant English headings','nested base URL','five viewport widths','GIF autoplay','two icon-only buttons','no static-image toolbar','play/stop toggle icons and labels','animated enlarge/Escape','language persists through navigation','Back','mobile menu','embed mode','direct file access','no-JS navigation','200% zoom']},null,2)+'\n');
  console.log(`PASS: ${results.length} page-language combinations; layout and interactions.`);
  await browser.close();server.close();
})().catch(e=>{console.error(e);server.close();process.exit(1);});
