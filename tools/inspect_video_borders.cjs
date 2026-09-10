/* Read-only border inspection. Uses an existing Playwright/Chromium installation.
 * Samples the entire duration; proposals require review before publication.
 */
const { chromium } = require(process.env.PLAYWRIGHT_MODULE || 'playwright');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
(async () => {
  const browser = await chromium.launch({headless: true, executablePath: process.env.CHROMIUM_PATH, args: ['--no-sandbox', '--allow-file-access-from-files']});
  try {
    const page = await browser.newPage();
    await page.goto('file://' + root + '/index.html');
    for (const file of fs.readdirSync(path.join(root, 'assets/media')).filter(f => f.endsWith('.mp4'))) {
      const result = await page.evaluate(async file => {
        const v = document.createElement('video');
        v.muted = true;
        v.src = 'assets/media/' + file;
        await new Promise((resolve, reject) => {v.onloadeddata = resolve; v.onerror = reject;});
        const canvas = document.createElement('canvas');
        canvas.width = v.videoWidth; canvas.height = v.videoHeight;
        const ctx = canvas.getContext('2d', {willReadFrequently: true});
        let left = canvas.width, top = canvas.height, right = -1, bottom = -1, samples = 0;
        for (let t = 0; t < v.duration; t += 0.25) {
          if (t > 0) await new Promise(resolve => {v.onseeked = resolve; v.currentTime = t;});
          ctx.drawImage(v, 0, 0);
          const data = ctx.getImageData(0, 0, canvas.width, canvas.height).data;
          for (let y = 0; y < canvas.height; y++) for (let x = 0; x < canvas.width; x++) {
            const i = (y * canvas.width + x) * 4;
            if (data[i] > 8 || data[i + 1] > 8 || data[i + 2] > 8) {
              left = Math.min(left, x); right = Math.max(right, x);
              top = Math.min(top, y); bottom = Math.max(bottom, y);
            }
          }
          samples++;
        }
        return {file, width: canvas.width, height: canvas.height, duration: v.duration, samples, bounds: [left, top, right + 1, bottom + 1]};
      }, file);
      console.log(JSON.stringify(result));
    }
  } finally { await browser.close(); }
})().catch(e => {console.error(e); process.exitCode = 1;});
