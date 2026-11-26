#!/usr/bin/env python3
"""Sugiere enlaces internos para un borrador a partir del corpus de artículos publicados.

Uso: python3 sugerir_enlaces.py borrador.json [--max 6]
El borrador es el documento del panel (con titulo y cuerpo_html). Puntúa cada artículo publicado por palabras en común
(los nombres propios pesan el doble) y propone los mejores que no estén ya enlazados. Piden 3-5 enlaces internos por artículo.
Usa corpus/AUTORES.tsv (74 artículos) y corpus/nuevos/*.json (los publicados después).
"""
import csv, glob, json, os, re, sys, unicodedata

AQUI = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(AQUI, "..", "corpus")
VACIAS = set("""para como pero esta este esto estos estas entre sobre desde hasta cuando donde porque aunque tiene tienen tener hace hacen
ser son fue fueron sido más menos muy también todo todos toda todas otro otra otros otras cada cual cuales sino solo según tras
nba temporada equipo equipos jugador jugadores partido partidos puntos año años dos tres cuatro primera primer segunda segundo""".split())


def norm(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def palabras(texto):
    return {norm(w) for w in re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ’'-]{5,}", texto) if norm(w) not in VACIAS}


def nombres(texto):
    return {norm(w) for w in re.findall(r"\b[A-ZÁÉÍÓÚÑ][a-záéíóúüñ]{3,}", texto)} - VACIAS


def articulos():
    out = {}
    with open(os.path.join(CORPUS, "AUTORES.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            out[r["url"]] = {"titulo": r["titulo"], "url": r["url"], "fecha": r["fecha"], "base": r["titulo"] + " " + r["slug"].replace("-", " ")}
    for ruta in glob.glob(os.path.join(CORPUS, "nuevos", "*.json")):
        d = json.load(open(ruta, encoding="utf-8"))
        t = d["title"].get("rendered", "") if isinstance(d["title"], dict) else d["title"]
        out[d["link"]] = {"titulo": t, "url": d["link"], "fecha": d["date"][:10], "base": t + " " + d["slug"].replace("-", " ")}
    return out


def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    doc = json.load(open(sys.argv[1], encoding="utf-8"))
    mx = int(sys.argv[sys.argv.index("--max") + 1]) if "--max" in sys.argv else 6
    html = doc.get("cuerpo_html", "")
    texto = re.sub(r"<[^>]+>", " ", re.sub(r"<!--.*?-->", "", html, flags=re.S))
    ya = set(re.findall(r'href="(https://undraftedzone\.com/[^"]+)"', html))
    mis_p, mis_n = palabras(doc.get("titulo", "") + " " + texto), nombres(doc.get("titulo", "") + " " + texto)
    propios = {doc.get("slug", "")}
    cand = []
    for a in articulos().values():
        if a["url"] in ya or any(s and s in a["url"] for s in propios):
            continue
        p = palabras(a["base"]); n = nombres(a["titulo"]) | {norm(w) for w in re.findall(r"[A-Za-z]{4,}", a["titulo"]) if w[0].isupper()}
        comunes_n = (mis_n & n) | (mis_n & p)
        comunes_p = (mis_p & p) - comunes_n
        puntos = 2 * len(comunes_n) + len(comunes_p)
        if puntos >= 2:
            cand.append((puntos, a, sorted(comunes_n | comunes_p)))
    cand.sort(key=lambda t: (-t[0], t[1]["fecha"]), reverse=False)
    print("Enlaces internos ya presentes: %d (se piden 3-5)" % len(ya))
    for puntos, a, c in cand[:mx]:
        print("%2d  %s  %s\n    %s\n    por: %s" % (puntos, a["fecha"], a["titulo"], a["url"], ", ".join(c[:8])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
