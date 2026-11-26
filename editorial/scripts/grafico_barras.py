#!/usr/bin/env python3
"""Gráfico propio de barras horizontales (sin fotos ni logos), con los colores de la web, en WebP de menos de 300 KB.

Con los datos de la instantánea (editorial/datos/ultimo/clasificacion.json):
  python3 grafico_barras.py --metrica dif_puntos --titulo "Diferencia de puntos por equipo" --resaltar MIL --salida g.webp
  python3 grafico_barras.py --metrica pct --titulo "Porcentaje de victorias" --resaltar MIL --salida g.webp

Con datos propios (lista JSON de {"etiqueta": "...", "valor": 12.3}):
  python3 grafico_barras.py --datos datos.json --titulo "..." --pie "Fuente: ESPN, 26-nov-2026" --salida g.webp

Métricas: pct (porcentaje de victorias), dif_puntos (diferencia de puntos), pts_favor, pts_contra.
"""
import argparse, io, json, os, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
AQUI = os.path.dirname(os.path.abspath(__file__))
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FONDO, TINTA, SUAVE, ACENTO, RESALTE = "#0B1B4D", "#F4EFE6", "#8F9BC4", "#4F6FE8", "#F28C28"


def datos_de(metrica):
    cl = json.load(open(os.path.join(AQUI, "..", "datos", "ultimo", "clasificacion.json"), encoding="utf-8"))
    out = []
    for abr, e in cl.items():
        if metrica == "pct":
            v = e["victorias"] / (e["victorias"] + e["derrotas"]) * 100
        elif metrica == "dif_puntos":
            v = float(e["dif_puntos"])
        else:
            v = float(e["pts_favor" if metrica == "pts_favor" else "pts_contra"])
        out.append({"etiqueta": abr, "valor": v})
    return out


def dibujar(datos, titulo, pie, resaltar, salida, decimales):
    datos = sorted(datos, key=lambda d: -d["valor"])
    img = Image.new("RGB", (W, H), FONDO)
    d = ImageDraw.Draw(img)
    f = lambda r, t: ImageFont.truetype(r, t)
    d.text((80, 50), "UNDRAFTED ZONE", font=f(SANS_B, 26), fill=SUAVE)
    d.text((80, 90), titulo, font=f(SERIF_B, 54), fill=TINTA)
    top, bajo = 190, H - 90
    n = len(datos)
    paso = (bajo - top) / n
    alto = max(8, int(paso * 0.68))
    vmin, vmax = min(0, min(x["valor"] for x in datos)), max(0, max(x["valor"] for x in datos))
    x0, x1 = 230, W - 170
    esc = lambda v: x0 + (v - vmin) / ((vmax - vmin) or 1) * (x1 - x0)
    cero = esc(0)
    tam = 22 if n <= 20 else 18
    for i, x in enumerate(datos):
        y = top + i * paso
        col = RESALTE if x["etiqueta"] == resaltar else ACENTO
        a, b = sorted((cero, esc(x["valor"])))
        d.rectangle([a, y, max(b, a + 2), y + alto], fill=col)
        d.text((80, y + alto / 2 - tam / 2 - 2), x["etiqueta"], font=f(SANS_B if x["etiqueta"] == resaltar else SANS, tam), fill=TINTA)
        txt = ("%." + str(decimales) + "f") % x["valor"]
        txt = txt.replace(".", ",")
        if x["valor"] >= 0:
            d.text((max(b, a) + 10, y + alto / 2 - tam / 2 - 2), txt, font=f(SANS, tam), fill=TINTA)
        else:
            d.text((a - 10 - d.textlength(txt, font=f(SANS, tam)), y + alto / 2 - tam / 2 - 2), txt, font=f(SANS, tam), fill=TINTA)
    d.line([cero, top - 6, cero, bajo], fill=SUAVE, width=2)
    if pie:
        d.text((80, H - 60), pie, font=f(SANS, 22), fill=SUAVE)
    q = 90
    while True:
        buf = io.BytesIO(); img.save(buf, "WEBP", quality=q, method=6)
        if buf.tell() <= 300 * 1024 or q <= 40: break
        q -= 8
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    open(salida, "wb").write(buf.getvalue())
    return buf.tell()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--metrica", choices=["pct", "dif_puntos", "pts_favor", "pts_contra"])
    ap.add_argument("--datos", help="JSON con [{etiqueta, valor}]")
    ap.add_argument("--titulo", required=True)
    ap.add_argument("--pie", default="")
    ap.add_argument("--resaltar", default="")
    ap.add_argument("--decimales", type=int, default=1)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    if not a.metrica and not a.datos:
        ap.error("indica --metrica o --datos")
    datos = json.load(open(a.datos, encoding="utf-8")) if a.datos else datos_de(a.metrica)
    meta = json.load(open(os.path.join(AQUI, "..", "datos", "ultimo", "meta.json"), encoding="utf-8"))
    pie = a.pie or ("Fuente: ESPN, partidos hasta el " + meta["hasta_partidos_del"])
    tam = dibujar(datos, a.titulo, pie, a.resaltar, a.salida, a.decimales)
    print("OK %s %d bytes" % (a.salida, tam))


if __name__ == "__main__":
    sys.exit(main())
