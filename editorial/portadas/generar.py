#!/usr/bin/env python3
"""Genera la portada de un artículo con plantilla (sin IA, sin fotos ni logos).

Formato: 1600×900 px, WebP, menos de 300 KB. Elementos:
- color de la franquicia (fondo),
- pista de cancha (líneas blancas finas),
- dato destacado grande (una cifra o palabra corta),
- titular corto y sello «Undrafted Zone».

Uso:
  python3 generar.py --salida ruta.webp --titulo "Lesión de..." \
      --dato "24,6" --dato-etiqueta "puntos por partido" \
      --franquicia "Brooklyn Nets" --color "#000000" --color-texto "#FFFFFF"

Si no se indica --color, usa el de la tabla FRANQUICIAS. Si el WebP sale por
encima de 300 KB, baja la calidad hasta cumplir el límite.
"""
import argparse
import io
import os
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 900
LIMITE_BYTES = 300 * 1024

FUENTE_SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
FUENTE_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FUENTE_SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Colores de franquicia (fondo, texto). Solo color; sin escudos ni logos.
FRANQUICIAS = {
    "Minnesota Timberwolves": ("#0C2340", "#78BE20"),
    "Brooklyn Nets": ("#000000", "#FFFFFF"),
    "Miami Heat": ("#98002E", "#F9A01B"),
    "Los Angeles Clippers": ("#1D428A", "#C8102E"),
    "Milwaukee Bucks": ("#00471B", "#EEE1C6"),
    "Oklahoma City Thunder": ("#007AC1", "#EF3B24"),
    "Philadelphia 76ers": ("#006BB6", "#ED174C"),
    "Sacramento Kings": ("#5A2D81", "#63727A"),
    "Utah Jazz": ("#002B5C", "#F9A01B"),
    "Chicago Bulls": ("#CE1141", "#000000"),
}
FONDO_NEUTRO = ("#1B1B1B", "#F4EFE6")


def fuente(ruta, tam):
    return ImageFont.truetype(ruta, tam)


def envolver(draw, texto, f, ancho_max):
    palabras, lineas, actual = texto.split(), [], ""
    for p in palabras:
        prueba = (actual + " " + p).strip()
        if draw.textlength(prueba, font=f) <= ancho_max:
            actual = prueba
        else:
            if actual:
                lineas.append(actual)
            actual = p
    if actual:
        lineas.append(actual)
    return lineas


def pista(draw, color):
    """Pista de cancha: línea central, círculo y áreas, en trazo fino."""
    grosor = 3
    x0, x1 = 1210, 1560  # todo a la derecha: el texto no pisa nunca la pista
    cy = H // 2
    draw.arc([x0 - 150, cy - 150, x0 + 150, cy + 150], 0, 360, fill=color, width=grosor)
    draw.line([x0, 40, x0, H - 40], fill=color, width=grosor)
    draw.rectangle([x1 - 120, cy - 170, x1, cy + 170], outline=color, width=grosor)
    draw.arc([x1 - 200, cy - 80, x1 - 40, cy + 80], 270, 90, fill=color, width=grosor)


def generar(salida, titulo, dato, dato_etiqueta, franquicia, color, color_texto):
    if color:
        fondo_hex, texto_hex = color, (color_texto or "#FFFFFF")
    else:
        fondo_hex, texto_hex = FRANQUICIAS.get(franquicia, FONDO_NEUTRO)
    fondo = Image.new("RGB", (W, H), fondo_hex)
    draw = ImageDraw.Draw(fondo)
    linea = tuple(int(texto_hex.lstrip("#")[i:i + 2], 16) for i in (0, 2, 4))
    pista(draw, (*linea, 70))  # fina y translúcida
    draw.rectangle([0, H - 14, W, H], fill=texto_hex)

    texto_rgb = color_texto or texto_hex
    x = 110
    # Dato destacado
    f_dato = fuente(FUENTE_SERIF, 300)
    draw.text((x, 150), dato, font=f_dato, fill=texto_rgb)
    f_et = fuente(FUENTE_SANS_REG, 46)
    draw.text((x + 8, 480), dato_etiqueta.upper(), font=f_et, fill=texto_rgb)

    # Titular
    f_tit = fuente(FUENTE_SANS, 64)
    y = 600
    for linea_txt in envolver(draw, titulo, f_tit, 1000)[:3]:
        draw.text((x, y), linea_txt, font=f_tit, fill=texto_rgb)
        y += 84

    # Sello
    f_sello = fuente(FUENTE_SANS, 34)
    draw.text((x, 70), "UNDRAFTED ZONE", font=f_sello, fill=texto_rgb)
    if franquicia:
        f_fr = fuente(FUENTE_SANS_REG, 30)
        draw.text((x, 820), franquicia.upper(), font=f_fr, fill=texto_rgb)

    calidad = 88
    while True:
        buf = io.BytesIO()
        fondo.save(buf, "WEBP", quality=calidad, method=6)
        if buf.tell() <= LIMITE_BYTES or calidad <= 40:
            break
        calidad -= 8
    os.makedirs(os.path.dirname(os.path.abspath(salida)), exist_ok=True)
    with open(salida, "wb") as fh:
        fh.write(buf.getvalue())
    return buf.tell(), calidad


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--salida", required=True)
    p.add_argument("--titulo", required=True)
    p.add_argument("--dato", required=True, help="Cifra o palabra corta (p. ej. 24,6)")
    p.add_argument("--dato-etiqueta", required=True)
    p.add_argument("--franquicia", default="", help="Nombre de la franquicia, o vacío si es evergreen")
    p.add_argument("--color", default="", help="Color de fondo en hex, si no es el de la tabla")
    p.add_argument("--color-texto", default="", help="Color del texto en hex")
    a = p.parse_args()
    tam, cal = generar(a.salida, a.titulo, a.dato, a.dato_etiqueta, a.franquicia, a.color, a.color_texto)
    print(f"OK {a.salida} {tam} bytes calidad {cal}")
    if tam > LIMITE_BYTES:
        print("AVISO: supera 300 KB", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
