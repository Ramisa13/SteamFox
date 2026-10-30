"""Fetch the latest Finnish spot electricity prices and save them to data/prices.json.

Source: Pörssisähkö.net (Nord Pool day-ahead, Finland area), prices in c/kWh including VAT.
Run by the GitHub Action in .github/workflows/prices.yml every afternoon.
"""
import datetime
import json
import os
import urllib.request

URL = "https://api.porssisahko.net/v1/latest-prices.json"

req = urllib.request.Request(URL, headers={"User-Agent": "SteamFox/1.0 (github.com/Ramisa13/SteamFox)"})
with urllib.request.urlopen(req, timeout=30) as resp:
    data = json.load(resp)

prices = sorted(
    (
        {"start": p["startDate"], "end": p["endDate"], "price": round(float(p["price"]), 3)}
        for p in data["prices"]
    ),
    key=lambda x: x["start"],
)
if not prices:
    raise SystemExit("No prices returned; keeping the previous file.")

out = {
    "source": "Pörssisähkö.net · Nord Pool day-ahead, Finland · c/kWh incl. VAT",
    "fetched_at": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
    "sample": False,
    "prices": prices,
}
os.makedirs("data", exist_ok=True)
with open("data/prices.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(f"Saved {len(prices)} price periods, {prices[0]['start']} → {prices[-1]['end']}")
