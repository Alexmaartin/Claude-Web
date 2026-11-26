#!/usr/bin/env python3
"""Instantánea diaria de datos de la NBA desde la API pública de ESPN (solo lectura).

Escribe en editorial/datos/ultimo/:
  clasificacion.json  balance, local/visitante, racha y diferencia de cada equipo
  jugadores.json      promedios por partido de todos los jugadores
  partidos.json       resultados de cada equipo, con fecha local de EE. UU., rival, sede y marcador
  meta.json           fecha de la instantánea y fuentes

Los agentes (que no pueden abrir ESPN) la leen con `git pull`; `verificar_cifras.py` compara contra ella.
Uso: python3 editorial/scripts/snapshot_datos.py [--temporada 2027]
"""
import argparse, datetime, json, os, sys, time, urllib.request
from zoneinfo import ZoneInfo

RAIZ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "datos", "ultimo")
UA = {"User-Agent": "Mozilla/5.0 (UndraftedZone datos)"}


def get(url, intentos=3):
    for i in range(intentos):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=40) as r:
                return json.load(r)
        except Exception as e:  # noqa: BLE001
            if i == intentos - 1:
                raise
            time.sleep(2 * (i + 1))


def clasificacion(temp):
    d = get("https://site.api.espn.com/apis/v2/sports/basketball/nba/standings?season=%s" % temp)
    out = {}

    def walk(n):
        if "standings" in n:
            for e in n["standings"]["entries"]:
                s = {x["name"]: x.get("displayValue") for x in e["stats"]}
                out[e["team"]["abbreviation"]] = {
                    "equipo": e["team"]["displayName"], "victorias": int(s["wins"]), "derrotas": int(s["losses"]),
                    "pct": s.get("winPercent"), "local": s.get("Home"), "visitante": s.get("Road"),
                    "ultimos10": s.get("Last Ten Games"), "racha": s.get("streak"),
                    "dif_puntos": s.get("pointDifferential"), "pts_favor": s.get("avgPointsFor"), "pts_contra": s.get("avgPointsAgainst"),
                }
        for c in n.get("children", []):
            walk(c)
    walk(d)
    return out


def jugadores(temp):
    base = ("https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/statistics/byathlete?region=us&lang=en&contentorigin=espn"
            "&isqualified=false&page=%d&limit=200&sort=offensive.avgPoints%%3Adesc&season=" + str(temp) + "&seasontype=2")
    out, p = {}, 1
    while True:
        d = get(base % p)
        cats = {c["name"]: c["names"] for c in d["categories"]}
        for x in d["athletes"]:
            g = dict(zip(cats["general"], x["categories"][0]["values"]))
            o = dict(zip(cats["offensive"], x["categories"][1]["values"]))
            a = x["athlete"]
            out[a["id"]] = {
                "nombre": a["displayName"], "equipo": a.get("teamShortName"), "pj": int(g["gamesPlayed"]), "min": round(g["avgMinutes"], 1),
                "pts": round(o["avgPoints"], 1), "reb": round(g["avgRebounds"], 1), "ast": round(o["avgAssists"], 1),
                "fg": round(o["fieldGoalPct"], 1), "tp": round(o["threePointFieldGoalPct"], 1),
            }
        if p >= d["pagination"]["pages"]:
            break
        p += 1
    return out


def partidos(temp, abreviaturas):
    # Fecha local de EE. UU.: Este para casi todos, Centro/Montaña/Pacífico no cambian el día de forma relevante en la práctica.
    tz = ZoneInfo("America/New_York")
    ids = get("https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams")["sports"][0]["leagues"][0]["teams"]
    out = {}
    for t in ids:
        t = t["team"]
        d = get("https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/%s/schedule?season=%s" % (t["id"], temp))
        lista = []
        for e in d["events"]:
            c = e["competitions"][0]
            if not c["status"]["type"]["completed"]:
                continue
            eq = {x["homeAway"]: x for x in c["competitors"]}
            mio = "home" if eq["home"]["team"]["abbreviation"] == t["abbreviation"] else "away"
            rival = eq["away" if mio == "home" else "home"]
            sc = lambda x: int((x["score"]["displayValue"] if isinstance(x["score"], dict) else x["score"]))
            fecha = datetime.datetime.fromisoformat(e["date"].replace("Z", "+00:00")).astimezone(tz).date().isoformat()
            lista.append({"fecha": fecha, "rival": rival["team"]["abbreviation"], "sede": "local" if mio == "home" else "visitante",
                          "resultado": "V" if eq[mio].get("winner") else "D", "puntos": sc(eq[mio]), "puntos_rival": sc(rival),
                          "copa": any("Cup" in (n.get("headline") or "") for n in c.get("notes", []))})
        lista.sort(key=lambda g: g["fecha"])
        out[t["abbreviation"]] = lista
        time.sleep(0.3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--temporada", default="2027")
    a = ap.parse_args()
    os.makedirs(RAIZ, exist_ok=True)
    cl = clasificacion(a.temporada)
    datos = {"clasificacion.json": cl, "jugadores.json": jugadores(a.temporada), "partidos.json": partidos(a.temporada, list(cl))}
    for nombre, contenido in datos.items():
        with open(os.path.join(RAIZ, nombre), "w", encoding="utf-8") as f:
            json.dump(contenido, f, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    meta = {"temporada": a.temporada, "fuente": "API pública de ESPN", "hasta_partidos_del": max((g[-1]["fecha"] for g in datos["partidos.json"].values() if g), default=None)}
    with open(os.path.join(RAIZ, "meta.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=1)
    print("OK", meta, {k: len(v) for k, v in datos.items()})


if __name__ == "__main__":
    sys.exit(main())
