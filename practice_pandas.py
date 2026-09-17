import pandas as pd

data = {
    "asset": ["USDC", "WETH", "DAI"],
    "supplied": [1000000, 2000000, 500000],
    "borrowed": [800000, 600000, 450000],
}
aave_table = pd.DataFrame(data)
aave_table["available"] = (
    aave_table["supplied"] - aave_table["borrowed"]
)
aave_table['utilization_pct'] = (
    aave_table["borrowed"] / aave_table["supplied"] * 100
)
# aave_table.sort_values("borrowed", ascending=False)   this command sorts the table so that the borrowed values are ranked from Highest to lowest
high_utilization = aave_table[aave_table["utilization_pct"] >= 80] # this is a filtered table that shows who carries utilization greater than 80 %

# print(high_utilization.sort_values(by="utilization_pct", ascending=False)) this command shows that filtered table and orders it by utilization percent from highest to lowest

available_markets = aave_table[aave_table["available"] >= 200000]

print(available_markets.sort_values(by="available", ascending=False))
