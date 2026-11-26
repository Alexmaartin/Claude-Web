#!/usr/bin/env python3
"""Copia de seguridad ligera del panel dentro del repositorio.

Entrada: carpeta que deja `ArtifactData` con `out_dir` (una subcarpeta por colección y un JSON por documento).
Salida:  editorial/backups/panel/latest/<colección>/<id>.json  (textos y campos, sin imágenes en base64)
         editorial/backups/panel/imagenes/<colección>--<id>--<campo>.<webp|jpg>  (cada imagen, solo si es nueva)

Uso: python3 copia_panel.py <carpeta_entrada> [--colecciones borradores ideas_evergreen ...]
Las imágenes se guardan como archivos (no dentro del JSON) para que el repositorio no crezca con cada copia diaria.
"""
import base64, hashlib, json, os, re, shutil, sys

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "backups", "panel")
DATA_URI = re.compile(r"^data:image/(webp|jpeg|png);base64,(.+)$", re.S)
EXT = {"webp": "webp", "jpeg": "jpg", "png": "png"}


def aligerar(valor, col, id_, campo, nuevas):
    if isinstance(valor, str):
        m = DATA_URI.match(valor)
        if not m:
            return valor
        binario = base64.b64decode(m.group(2))
        nombre = "%s--%s--%s.%s" % (col, id_, campo, EXT[m.group(1)])
        ruta = os.path.join(RAIZ, "imagenes", nombre)
        if not os.path.exists(ruta) or hashlib.md5(open(ruta, "rb").read()).hexdigest() != hashlib.md5(binario).hexdigest():
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            open(ruta, "wb").write(binario)
            nuevas.append(nombre)
        return "[imagen guardada en backups/panel/imagenes/%s]" % nombre
    if isinstance(valor, dict):
        return {k: aligerar(v, col, id_, campo + "." + k if campo else k, nuevas) for k, v in valor.items()}
    if isinstance(valor, list):
        return [aligerar(v, col, id_, "%s.%d" % (campo, i), nuevas) for i, v in enumerate(valor)]
    return valor


def main():
    a = sys.argv[1:]
    if not a:
        print(__doc__); return 2
    entrada = a[0]
    solo = a[a.index("--colecciones") + 1:] if "--colecciones" in a else None
    nuevas, total = [], 0
    for col in sorted(os.listdir(entrada)):
        carpeta = os.path.join(entrada, col)
        if not os.path.isdir(carpeta) or (solo and col not in solo):
            continue
        destino = os.path.join(RAIZ, "latest", col)
        shutil.rmtree(destino, ignore_errors=True)
        os.makedirs(destino, exist_ok=True)
        for f in sorted(os.listdir(carpeta)):
            if not f.endswith(".json"):
                continue
            id_ = f[:-5]
            doc = json.load(open(os.path.join(carpeta, f), encoding="utf-8"))
            ligero = aligerar(doc, col, id_, "", nuevas)
            json.dump(ligero, open(os.path.join(destino, f), "w", encoding="utf-8"), ensure_ascii=False, indent=1, sort_keys=True)
            total += 1
    print("Copiados %d documentos; imágenes nuevas: %d" % (total, len(nuevas)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
