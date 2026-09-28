import requests
import json
import csv
import os
import requests

API_URL = "https://api.v3.aave.com/graphql"
# Aave v3 Ethereum market
MARKET_ADDRESS = "0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2"

QUERY = """
{
  market(request: { address: "0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2", chainId: 1 }) {
    name
    reserves {
      underlyingToken { symbol }
      size { usd }
      borrowInfo { total { usd } availableLiquidity { usd } }
    }
  }
}
"""


def fetch_reserves():
    response = requests.post(API_URL, json={"query": QUERY}, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]["market"]["reserves"]


def clean(reserves):
    """Turn raw API reserves into clean rows. Skips reserves with missing data."""
    rows = []
    skipped = []
    for reserve in reserves:
        symbol = reserve["underlyingToken"]["symbol"]
        try:
            supplied = float(reserve["size"]["usd"])
            borrowed = float(reserve["borrowInfo"]["total"]["usd"])
            available = float(reserve["borrowInfo"]["availableLiquidity"]["usd"])
        except (TypeError, KeyError):
            skipped.append(symbol)
            continue
        rows.append(
            {
                "symbol": symbol,
                "supplied_usd": supplied,
                "borrowed_usd": borrowed,
                "available_liquidity_usd": available,
            }
        )
    return rows, skipped


def main():
    reserves = fetch_reserves()
    rows, skipped = clean(reserves)

    os.makedirs("data", exist_ok=True)
    path = "data/aave_v3_ethereum_reserves.csv"
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "symbol",
                "supplied_usd",
                "borrowed_usd",
                "available_liquidity_usd",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} reserves to {path}")
    if skipped:
        print(f"Skipped {len(skipped)} reserve(s) with missing data: {', '.join(skipped)}")


if __name__ == "__main__":
    main()
