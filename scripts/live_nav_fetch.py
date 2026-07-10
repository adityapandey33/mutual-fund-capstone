from pathlib import Path
import pandas as pd
import requests

BASE = Path(__file__).resolve().parent
RAW = BASE / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

SCHEMES = {
    "125497": "HDFC Top 100 Direct",
    "119551": "SBI Bluechip",
    "120503": "ICICI Bluechip",
    "118632": "Nippon Large Cap",
    "119092": "Axis Bluechip",
    "120841": "Kotak Bluechip",
}

for code, label in SCHEMES.items():
    url = f"https://api.mfapi.in/mf/{code}"
    res = requests.get(url, timeout=30)
    res.raise_for_status()
    payload = res.json()
    meta = payload.get("meta", {})
    df = pd.DataFrame(payload.get("data", []))

    if df.empty:
        print(f"No NAV rows for {code} - {label}")
        continue

    df["scheme_code"] = code
    df["scheme_name"] = meta.get("scheme_name", label)
    out = RAW / f"live_nav_{code}.csv"
    df.to_csv(out, index=False)
    print(f"Saved {out.name}: {len(df)} rows; latest NAV {df.iloc[0]['nav']} on {df.iloc[0]['date']}")