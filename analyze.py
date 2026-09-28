import pandas as pd

aave_table = pd.read_csv("data/aave_v3_ethereum_reserves.csv")

aave_table["utilization_pct"] = aave_table["borrowed_usd"] / aave_table["supplied_usd"] * 100

stablecoins = ["USDC", "USDT", "DAI", "FRAX", "PYUSD", "GHO"]
no_stables = aave_table[~aave_table["symbol"].isin(stablecoins)]
big_markets = no_stables[no_stables["supplied_usd"] > 1_000_000]

result = big_markets.sort_values("utilization_pct", ascending=False).head(5)
print(result[["symbol", "supplied_usd", "utilization_pct"]])

