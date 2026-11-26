#!/usr/bin/env python3
"""Consulta de solo lectura a Google Search Console (sin probar: falta la clave de la cuenta de servicio).

Uso:
  GSC_SERVICE_ACCOUNT_JSON='{...}' python3 search_console.py --dias 7 [--sitio sc-domain:undraftedzone.com]

Imprime un JSON con páginas y consultas (clics, impresiones, CTR, posición). Necesita `cryptography` o `google-auth`.
La clave solo se lee de la variable de entorno; nunca se escribe en disco ni se imprime.
"""
import argparse, base64, datetime, json, os, sys, time, urllib.parse, urllib.request

ALCANCE = "https://www.googleapis.com/auth/webmasters.readonly"


def token(clave):
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding
    except ImportError:
        sys.exit("Falta la librería cryptography (pip install cryptography)")
    b64 = lambda b: base64.urlsafe_b64encode(b).rstrip(b"=")
    ahora = int(time.time())
    cab = b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    cuerpo = b64(json.dumps({"iss": clave["client_email"], "scope": ALCANCE, "aud": "https://oauth2.googleapis.com/token", "iat": ahora, "exp": ahora + 3000}).encode())
    firma = serialization.load_pem_private_key(clave["private_key"].encode(), None).sign(cab + b"." + cuerpo, padding.PKCS1v15(), hashes.SHA256())
    jwt = (cab + b"." + cuerpo + b"." + b64(firma)).decode()
    datos = urllib.parse.urlencode({"grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer", "assertion": jwt}).encode()
    with urllib.request.urlopen(urllib.request.Request("https://oauth2.googleapis.com/token", datos), timeout=30) as r:
        return json.load(r)["access_token"]


def consulta(tok, sitio, dim, ini, fin, limite=25):
    url = "https://searchconsole.googleapis.com/webmasters/v3/sites/%s/searchAnalytics/query" % urllib.parse.quote(sitio, safe="")
    cuerpo = json.dumps({"startDate": ini, "endDate": fin, "dimensions": [dim], "rowLimit": limite}).encode()
    req = urllib.request.Request(url, cuerpo, {"Authorization": "Bearer " + tok, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        filas = json.load(r).get("rows", [])
    return [{"clave": f["keys"][0], "clics": f["clicks"], "impresiones": f["impressions"], "ctr": round(f["ctr"] * 100, 2), "posicion": round(f["position"], 1)} for f in filas]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=7)
    ap.add_argument("--sitio", default="sc-domain:undraftedzone.com")
    a = ap.parse_args()
    bruto = os.environ.get("GSC_SERVICE_ACCOUNT_JSON")
    if not bruto:
        sys.exit("Falta GSC_SERVICE_ACCOUNT_JSON en el entorno")
    tok = token(json.loads(bruto))
    fin = datetime.date.today() - datetime.timedelta(days=2)  # Search Console tarda 2 días en consolidar
    ini = fin - datetime.timedelta(days=a.dias - 1)
    print(json.dumps({"desde": str(ini), "hasta": str(fin), "paginas": consulta(tok, a.sitio, "page", str(ini), str(fin)), "consultas": consulta(tok, a.sitio, "query", str(ini), str(fin))}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
