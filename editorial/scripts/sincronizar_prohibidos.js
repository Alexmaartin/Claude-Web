#!/usr/bin/env node
/* Copia editorial/terminos_prohibidos.json dentro de editorial/panel.html (entre las marcas PROHIBIDOS:inicio y PROHIBIDOS:fin).
 * Uso: node editorial/scripts/sincronizar_prohibidos.js [--comprobar]   (con --comprobar solo avisa si el panel va desfasado) */
const fs = require('fs');
const path = require('path');
const raiz = path.join(__dirname, '..');
const lista = JSON.parse(fs.readFileSync(path.join(raiz, 'terminos_prohibidos.json'), 'utf8'));
const { nota, ...datos } = lista;
const bloque = '/* PROHIBIDOS:inicio (generado por scripts/sincronizar_prohibidos.js) */\nconst PROHIBIDOS = ' + JSON.stringify(datos) + ';\n/* PROHIBIDOS:fin */';
const ruta = path.join(raiz, 'panel.html');
const html = fs.readFileSync(ruta, 'utf8');
const re = /\/\* PROHIBIDOS:inicio[\s\S]*?\/\* PROHIBIDOS:fin \*\//;
if (!re.test(html)) { console.error('No encuentro las marcas PROHIBIDOS en panel.html'); process.exit(2); }
const nuevo = html.replace(re, () => bloque);
if (process.argv.includes('--comprobar')) {
  if (nuevo !== html) { console.error('El panel NO está sincronizado con terminos_prohibidos.json'); process.exit(1); }
  console.log('Panel sincronizado'); process.exit(0);
}
fs.writeFileSync(ruta, nuevo);
console.log(nuevo === html ? 'Sin cambios' : 'panel.html actualizado');
