/* Uso: node captura.js <salida-dir> [vista]
   Renderiza editorial/panel.html con el arnés (datos de ejemplo) en móvil 400 px y escritorio. */
const path = require('path');
const fs = require('fs');
const { chromium } = require('playwright');
const out = process.argv[2] || '.';
const vistas = (process.argv[3] || 'hoy,borradores,ideas,metricas').split(',');
const repo = path.resolve(__dirname, '..', '..', '..');
const panel = 'file://' + path.join(repo, 'editorial', 'panel.html');
const stub = fs.readFileSync(path.join(__dirname, 'stub-db.js'), 'utf8');
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const perfiles = [['movil', { viewport: { width: 400, height: 860 }, deviceScaleFactor: 2, isMobile: true }], ['escritorio', { viewport: { width: 1280, height: 900 }, deviceScaleFactor: 1 }]];
  for (const [nombre, opts] of perfiles) {
    for (const v of vistas) {
      const ctx = await browser.newContext({ ...opts, colorScheme: 'light' });
      await ctx.addInitScript(stub);
      const page = await ctx.newPage();
      const errores = [];
      page.on('pageerror', (e) => errores.push(String(e)));
      await page.goto(panel + '#' + v);
      await page.waitForTimeout(700);
      const desbordes = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      await page.screenshot({ path: path.join(out, `${nombre}-${v}.png`), fullPage: true });
      console.log(`${nombre} ${v}: desborde horizontal ${desbordes}px, errores ${errores.length ? errores.join(' | ') : 'ninguno'}`);
      await ctx.close();
    }
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
