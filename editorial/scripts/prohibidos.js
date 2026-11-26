/* Comprobación de términos prohibidos con la lista única (editorial/terminos_prohibidos.json).
 * Uso como módulo: const { analizar } = require('./prohibidos'); analizar(texto) -> { bloquea: [...], revisar: [...], sustituir: [...] }
 * Uso desde la terminal: node prohibidos.js "texto a comprobar"
 */
const fs = require('fs');
const path = require('path');
const lista = JSON.parse(fs.readFileSync(path.join(__dirname, '..', 'terminos_prohibidos.json'), 'utf8'));

const norm = s => String(s || '').normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase();

function analizar(texto, l = lista) {
  const t = norm(texto);
  const hallar = (subs, regs) => {
    const out = [];
    for (const s of subs || []) if (t.includes(norm(s))) out.push(s);
    for (const r of regs || []) { const m = new RegExp(r, 'i').exec(t); if (m) out.push(m[0]); }
    return [...new Set(out)];
  };
  const sustituir = Object.keys(l.sustituir || {}).filter(k => t.includes(norm(k)));
  return { bloquea: hallar(l.bloquea, l.regex_bloquea), revisar: hallar(l.revisar, l.regex_revisar), sustituir };
}

module.exports = { analizar, lista };

if (require.main === module) {
  const r = analizar(process.argv.slice(2).join(' '));
  console.log(JSON.stringify(r));
  process.exit(r.bloquea.length ? 1 : 0);
}
