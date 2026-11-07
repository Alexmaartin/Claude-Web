#!/usr/bin/env node
/*
 * Comprobaciones de un borrador antes de aprobarlo o subirlo.
 * Uso: node comprobar_borrador.js <borrador.json> [--slugs slugs.txt]
 *   borrador.json: documento de la colección borradores (exportado con ArtifactData).
 *   --slugs: lista de slugs publicados válidos, uno por línea (para enlaces internos).
 * Sale con código 1 si hay algún FALLO. Los AVISOS no bloquean.
 */
const fs = require('fs');

const args = process.argv.slice(2);
if (!args[0]) { console.error('Uso: node comprobar_borrador.js <borrador.json> [--slugs fichero]'); process.exit(2); }
const doc = JSON.parse(fs.readFileSync(args[0], 'utf8'));
const d = doc.data || doc;
const iSlugs = args.indexOf('--slugs');
const slugsValidos = iSlugs > -1 ? new Set(fs.readFileSync(args[iSlugs + 1], 'utf8').split('\n').map(s => s.trim()).filter(Boolean)) : null;

const fallos = [], avisos = [], ok = [];
const check = (cond, msg, tipo = 'fallo') => (cond ? ok : (tipo === 'fallo' ? fallos : avisos)).push(msg);

const html = String(d.cuerpo_html || '');
const texto = html.replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
const palabras = texto ? texto.split(' ').length : 0;
const hrefs = [...html.matchAll(/href="([^"]+)"/g)].map(m => m[1]);
const internos = hrefs.filter(h => /^https:\/\/undraftedzone\.com\//.test(h));
const externos = hrefs.filter(h => !/^https:\/\/undraftedzone\.com\//.test(h));

// Título, extracto y slug
const t = String(d.titulo || '');
check(t.length >= 50 && t.length <= 65, `Titular de ${t.length} caracteres (50–65)`, 'aviso');
const ex = String(d.extracto || '');
check(ex.length >= 140 && ex.length <= 160, `Extracto de ${ex.length} caracteres (140–160)`);
check(/^[a-z0-9]+(-[a-z0-9]+)*$/.test(String(d.slug || '')), 'Slug con formato válido');
check(String(d.meta_descripcion || '').length > 0 || d.tipo !== 'guia', 'Meta descripción presente (guías)', 'aviso');
check(String(d.seo_titulo || '').length > 0 || d.tipo !== 'guia', 'Título SEO presente (guías)', 'aviso');

// Cuerpo
check(palabras >= 600, `Cuerpo de ${palabras} palabras (mínimo 600)`);
check(d.tipo !== 'guia' || palabras >= 1500, `Guía de ${palabras} palabras (objetivo 1.500)`, 'aviso');
const h2 = (html.match(/<h2>/g) || []).length;
check(d.tipo !== 'guia' || h2 >= 4, `Guía con ${h2} H2`, 'aviso');

// Enlaces
check(internos.length >= 3, `${internos.length} enlaces internos (mínimo 3)`);
check(internos.length <= 5, `${internos.length} enlaces internos (máximo recomendado 5)`, 'aviso');
check(externos.length === 0, `Sin enlaces externos en el cuerpo (encontrados ${externos.length})`);
if (slugsValidos) {
  const rotos = internos.filter(h => !slugsValidos.has(h.replace('https://undraftedzone.com/', '').replace(/\/$/, '')));
  check(rotos.length === 0, rotos.length ? `Enlaces internos que no existen: ${rotos.join(', ')}` : 'Todos los enlaces internos existen');
}

// Portada
const img = String(d.imagen_url || '');
check(/^data:image\/webp;base64,/.test(img), 'Portada WebP embebida');
check(img.length * 0.75 < 300 * 1024, `Portada de ${Math.round(img.length * 0.75 / 1024)} KB (máximo 300)`);

// Fuentes e higiene
check(Array.isArray(d.fuentes) && d.fuentes.length > 0, 'Fuentes registradas en el campo fuentes');
const todo = [t, ex, texto, String(d.pie_instagram || '')].join(' ').toLowerCase();
const prohibidos = ['apuest', 'cuota', 'odds', 'bookmaker', 'casino', 'parlay', 'hándicap', 'handicap'];
const hallados = prohibidos.filter(p => todo.includes(p));
check(hallados.length === 0, hallados.length ? `Términos de apuestas encontrados: ${hallados.join(', ')}` : 'Sin términos de apuestas');
check(!/salary cap|cap space/i.test(todo), 'Sin «salary cap» ni «cap space» (usar espacio salarial)', 'aviso');
check(!/\bsorteo\b|\blotería\b/i.test(todo) || /sorteo del draft/i.test(todo), 'Sin «lotería» suelta (solo «sorteo del draft»)', 'aviso');

console.log(`Borrador: ${d.titulo || '(sin titular)'} [${d.tipo || 'sin tipo'}]`);
for (const m of fallos) console.log('  FALLO  ' + m);
for (const m of avisos) console.log('  AVISO  ' + m);
for (const m of ok) console.log('  OK     ' + m);
console.log(fallos.length ? `\nResultado: NO LISTO (${fallos.length} fallos, ${avisos.length} avisos)` : `\nResultado: LISTO (${avisos.length} avisos)`);
process.exit(fallos.length ? 1 : 0);
