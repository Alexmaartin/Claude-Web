#!/usr/bin/env python3
"""Comprobación determinista de cifras contra la instantánea de datos (editorial/datos/ultimo/).

Ejemplos:
  python3 verificar_cifras.py equipo MIL                 # balance, local/visitante, racha, últimos 10, mayor racha de derrotas
  python3 verificar_cifras.py equipo MIL --tras 14 16    # balance tras 14 y tras 16 partidos
  python3 verificar_cifras.py jugador "Burries"          # promedios del jugador
  python3 verificar_cifras.py vivo cuerpo.json           # compara los bloques stats de un artículo vivo con los datos
  python3 verificar_cifras.py frescura                   # hasta qué partido llegan los datos

`cuerpo.json` es el documento del borrador (con `cuerpo_html`). Si los datos tienen más de 2 días, avisa.
Salida con código 1 si algún bloque no coincide.
"""
import datetime, json, os, re, sys, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
DATOS = os.path.join(AQUI, "..", "datos", "ultimo")
IDS = os.path.join(AQUI, "..", "vivos", "rookies-ids.json")


def cargar(n):
    with open(os.path.join(DATOS, n), encoding="utf-8") as f:
        return json.load(f)


def sin_acentos(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def frescura():
    m = cargar("meta.json")
    hoy = datetime.date.today()
    ult = datetime.date.fromisoformat(m["hasta_partidos_del"])
    dias = (hoy - ult).days
    print("Datos hasta los partidos del %s (hace %d días)." % (ult, dias))
    if dias > 2:
        print("AVISO: los datos pueden estar desfasados; ejecuta snapshot_datos.py.")
    return dias


def equipo(abr, tras):
    cl = cargar("clasificacion.json").get(abr.upper())
    ps = cargar("partidos.json").get(abr.upper())
    if not cl or ps is None:
        sys.exit("Equipo desconocido: %s" % abr)
    print("%s: %d-%d (%s), local %s, visitante %s, últimos 10 %s, racha %s" % (cl["equipo"], cl["victorias"], cl["derrotas"], cl["pct"], cl["local"], cl["visitante"], cl["ultimos10"], cl["racha"]))
    mejor = act = 0
    for g in ps:
        act = act + 1 if g["resultado"] == "D" else 0
        mejor = max(mejor, act)
    print("Mayor racha de derrotas esta temporada: %d (racha actual de derrotas: %d)" % (mejor, act))
    for n in tras:
        v = sum(1 for g in ps[:n] if g["resultado"] == "V")
        print("Tras %d partidos: %d-%d (hay %d jugados)" % (n, v, min(n, len(ps)) - v, len(ps)))


def jugador(texto):
    q = sin_acentos(texto)
    hallados = [(i, j) for i, j in cargar("jugadores.json").items() if q in sin_acentos(j["nombre"])]
    if not hallados:
        sys.exit("Sin coincidencias para %r" % texto)
    for i, j in hallados[:8]:
        print("%s (%s, %s): %d PJ, %s min, %s pts, %s reb, %s ast, %s%% TC, %s%% 3P" % (j["nombre"], i, j["equipo"], j["pj"], j["min"], j["pts"], j["reb"], j["ast"], j["fg"], j["tp"]))


NUM = r"(\d+(?:[’'.]\d+)?)"
BLOQUE = re.compile(r"<!--\s*stats:([a-z0-9-]+):inicio\s*-->.*?<p>\s*Partidos:\s*(\d+)\s*\((\d+) como titular\)\.\s*Minutos:\s*" + NUM + r"\.\s*Puntos:\s*" + NUM + r"\.\s*Rebotes:\s*" + NUM + r"\.\s*Asistencias:\s*" + NUM + r"\.\s*Tiros de campo:\s*" + NUM + r"%\.\s*Triples:\s*" + NUM + r"%\.", re.S)


def vivo(ruta):
    doc = json.load(open(ruta, encoding="utf-8"))
    html = doc.get("cuerpo_html", doc)
    ids = json.load(open(IDS, encoding="utf-8"))
    jug = cargar("jugadores.json")
    num = lambda s: float(s.replace("’", ".").replace("'", "."))
    fallos = 0
    bloques = BLOQUE.findall(html)
    if not bloques:
        sys.exit("No encuentro bloques stats con el formato esperado")
    for slug, pj, tit, mi, pt, rb, at, fg, tp in bloques:
        j = jug.get(ids.get(slug, ""))
        if not j:
            print("?  %-10s sin id en rookies-ids.json o sin datos" % slug); fallos += 1; continue
        pares = [("PJ", int(pj), j["pj"]), ("MIN", num(mi), j["min"]), ("PTS", num(pt), j["pts"]), ("REB", num(rb), j["reb"]), ("AST", num(at), j["ast"]), ("TC%", num(fg), j["fg"]), ("3P%", num(tp), j["tp"])]
        mal = [(n, a, b) for n, a, b in pares if abs(a - b) > 0.051]
        if mal:
            fallos += 1
            print("X  %-10s %s" % (slug, "; ".join("%s texto %s / datos %s" % m for m in mal)))
        else:
            print("OK %-10s (%d PJ, %s pts)" % (slug, j["pj"], j["pts"]))
    print("Titularidades no se comprueban con esta instantánea (usar la ficha del jugador).")
    frescura()
    return 1 if fallos else 0


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return 2
    if a[0] == "frescura":
        frescura(); return 0
    if a[0] == "equipo" and len(a) >= 2:
        equipo(a[1], [int(x) for x in a[a.index("--tras") + 1:]] if "--tras" in a else []); return 0
    if a[0] == "jugador" and len(a) >= 2:
        jugador(" ".join(a[1:])); return 0
    if a[0] == "vivo" and len(a) >= 2:
        return vivo(a[1])
    print(__doc__); return 2


if __name__ == "__main__":
    sys.exit(main())
