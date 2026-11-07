/* Arnés de pruebas del panel. DATOS DE EJEMPLO: no son reales.
   Simula window.claude.use('db') con la misma forma de colecciones que el panel espera. */
(function () {
  const hoy = new Date();
  const iso = (d) => new Date(hoy.getTime() - d * 3600e3).toISOString();
  const ejemplo = {
    borradores: [
      { id: 'b-ej-1', titulo: 'Lesión de ejemplo en el tobillo de un jugador ficticio antes de playoffs', slug: 'lesion-ejemplo-tobillo-playoffs-2027', extracto: 'Texto de ejemplo. Un jugador ficticio sufre una lesión leve y su equipo confirma que llegará a la siguiente ronda con dudas, según la fuente oficial de ejemplo.', etiquetas: ['nba', 'lesiones', 'ejemplo'], pie_instagram: 'Pie de ejemplo para Instagram.', cuerpo_html: '<p>Cuerpo de ejemplo. ' + 'Palabra de relleno '.repeat(120) + '</p><p><a href="https://undraftedzone.com/x">interno</a> <a href="https://ejemplo.com/">externo</a></p>', fuentes: ['https://ejemplo.com/fuente'], confianza: 'alta', estado: 'pendiente_revision', fecha: iso(3), actualizado_en: iso(3), imagen_url: '', noticia_id: 'n-ej-1',
        verificacion: { fecha: iso(2), confirmadas: 5, corregidas: 1, sin_comprobar: 1, pendientes_humano: ['Revisar cifra de minutos: fuente secundaria'] } },
      { id: 'b-ej-2', titulo: 'Borrador de ejemplo ya aprobado para comprobar la lista', slug: 'borrador-ejemplo-aprobado', extracto: 'Extracto de ejemplo de prueba para la vista de lista.', etiquetas: ['nba'], cuerpo_html: '<p>Cuerpo corto de ejemplo.</p>', fuentes: [], confianza: 'media', estado: 'aprobado', fecha: iso(30), actualizado_en: iso(30), imagen_url: '' },
    ],
    ideas_evergreen: [
      { id: 'i-ej-1', titulo: 'Idea de ejemplo para decidir', angulo: 'Ángulo de ejemplo.', estado: 'propuesta', fecha: iso(5) },
      { id: 'i-ej-2', titulo: 'Idea de ejemplo en cola', angulo: 'Otro ángulo.', estado: 'aprobada', fecha: iso(50) },
    ],
    incidencias_seo: [
      { id: 's-ej-1', problema: 'Incidencia SEO de ejemplo', pagina: '/ejemplo', prioridad: 'media', sugerencia: 'Sugerencia de ejemplo', estado: 'abierta' },
    ],
    alertas: [
      { id: 'a-ej-1', tipo: 'incertidumbre', mensaje: 'Alerta de ejemplo: dato sin confirmar', contexto: 'Contexto de ejemplo.', estado: 'abierta', fecha: iso(4) },
      { id: 'a-ej-2', tipo: 'tecnica', mensaje: 'Alerta técnica de ejemplo ya cerrada', contexto: '', estado: 'resuelta', fecha: iso(60) },
    ],
    ediciones: [
      { id: 'e-ej-1', borrador_id: 'b-ej-1', fecha: iso(2), antes: { titulo: 'Titular anterior de ejemplo' }, despues: { titulo: 'Lesión de ejemplo en el tobillo de un jugador ficticio antes de playoffs' } },
    ],
    noticias: [],
    metricas: [
      { id: 'web', actualizado: iso(2), articulos_publicados: 42,
        periodos: {
          dia: { visitas: 1280, visitas_previas: 1100, peticiones: 4100, serie: Array.from({ length: 24 }, (_, i) => ({ dia: 'h' + i, visitas: 20 + ((i * 37) % 90) })), top: [{ ruta: '/ejemplo-1', visitas: 320, cambio: 12, tipo: 'artículo' }, { ruta: '/.env', visitas: 700 }], procedencia: [{ origen: 'Google', visitas: 800 }, { origen: 'Directo', visitas: 300 }, { origen: 'Instagram', visitas: 180 }], articulos: [{ url: 'https://undraftedzone.com/ejemplo-1', titulo: 'Artículo de ejemplo', vistas: 320 }], dispositivos: [{ tipo: 'mobile', visitas: 900 }, { tipo: 'desktop', visitas: 380 }], paises: [{ pais: 'España', visitas: 1000 }, { pais: 'México', visitas: 280 }] },
          semana: { visitas: 8400, visitas_previas: 7900, peticiones: 26000, serie: Array.from({ length: 7 }, (_, i) => ({ dia: '2026-11-0' + (i + 1), visitas: 900 + i * 120 })), top: [{ ruta: '/ejemplo-1', visitas: 2100, cambio: 8, tipo: 'artículo' }, { ruta: '/ejemplo-2', visitas: 1300, cambio: -4 }, { ruta: '/wp-login.php', visitas: 900 }], procedencia: [{ origen: 'Google', visitas: 5000 }, { origen: 'Directo', visitas: 2000 }, { origen: 'Instagram', visitas: 900 }], articulos: [{ url: 'https://undraftedzone.com/ejemplo-1', titulo: 'Artículo de ejemplo', vistas: 2100 }], dispositivos: [{ tipo: 'mobile', visitas: 5600 }, { tipo: 'desktop', visitas: 2800 }], paises: [{ pais: 'España', visitas: 6000 }] },
          mes: { visitas: 31000, visitas_previas: 28000, peticiones: 95000, serie: Array.from({ length: 30 }, (_, i) => ({ dia: '2026-10-' + String(i + 1).padStart(2, '0'), visitas: 800 + ((i * 53) % 400) })), top: [], procedencia: [], articulos: [] },
        },
        cwv: [], tendencia_semanal: [] },
    ],
  };

  // Vista previa: no hay base real. Las escrituras se simulan en memoria.
  function coleccion(nombre) {
    const docs = () => (ejemplo[nombre] || []);
    return {
      doc(id) {
        return {
          update: async (patch) => { const d = docs().find((x) => x.id === id); if (d) Object.assign(d, patch); return true; },
          delete: async () => { const i = docs().findIndex((x) => x.id === id); if (i >= 0) docs().splice(i, 1); return true; },
        };
      },
      add: async (data) => { (ejemplo[nombre] = ejemplo[nombre] || []).push({ id: 'nuevo-' + Date.now(), ...data }); return true; },
      onSnapshot(ok) {
        setTimeout(() => ok({ docs: docs().map((d) => ({ id: d.id, exists: true, data: () => { const { id, ...r } = d; return r; } })) }), 0);
        return () => {};
      },
    };
  }
  const db = { collection: coleccion };
  window.claude = { use: async (nombre) => (nombre === 'db' ? db : null) };
  // El artifact publicado añade esta etiqueta viewport; en local hace falta para que 400 px sea de verdad 400 px.
  document.addEventListener('DOMContentLoaded', () => {
    const m = document.createElement('meta');
    m.name = 'viewport';
    m.content = 'width=device-width,initial-scale=1,viewport-fit=cover';
    document.head.appendChild(m);
  });
  window.__ejemplo = ejemplo;
})();
