const {chromium} = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const assert = require('node:assert/strict');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
(async () => {
  const browser = await chromium.launch({headless:true, executablePath:process.env.CHROMIUM_PATH, args:['--no-sandbox']});
  try {
    const page = await browser.newPage();
    for (const [name, video] of [['dashboard','panel_pre_01'], ['simulator','sim_02'], ['replay','replay_03']]) {
      await page.goto('file://' + root + '/' + name + '.html?lang=ko');
      const frame = page.locator('.media-frame').filter({has:page.locator(`video[src$="${video}.mp4"]`)});
      await frame.locator('video').evaluate(v => new Promise(resolve => {if(v.readyState >= 2) resolve(); else v.onloadeddata = resolve;}));
      for (const width of [390, 1440]) {
        await page.setViewportSize({width, height:1000});
        assert(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1));
        await frame.scrollIntoViewIfNeeded();
        const check = await frame.evaluate(f => {
          const picture = f.querySelector('.media-viewport').getBoundingClientRect();
          const buttons = [...f.querySelectorAll('button')].map(b => b.getBoundingClientRect());
          const outer = f.getBoundingClientRect();
          return buttons.every(b => b.top >= picture.bottom && b.bottom <= outer.bottom && b.left >= outer.left && b.right <= outer.right);
        });
        assert(check, 'Controls must remain below picture and inside frame');
      }
      await frame.locator('[data-play]').click();
      assert(await frame.locator('video').evaluate(v => v.paused));
      const time = await frame.locator('video').evaluate(v => v.currentTime);
      await frame.screenshot({path:path.join(root, 'docs/verification', video + '-cropped.png')});
      await frame.locator('[data-enlarge]').click();
      assert(await page.locator('dialog').evaluate(d => d.open));
      assert(await frame.locator('video').evaluate(v => v.paused));
      assert.equal(await frame.locator('video').evaluate(v => v.currentTime), time);
      await page.keyboard.press('Escape');
      await frame.locator('[data-play]').click();
      await page.waitForTimeout(200);
      assert(await frame.locator('video').evaluate(v => !v.paused));
      console.log('PASS', name, 'crop layout, control placement, pause/enlarge/resume');
    }
  } finally { await browser.close(); }
})().catch(e => {console.error(e);process.exitCode = 1;});
