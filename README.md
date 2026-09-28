# aave-market-analysis
Exploring liquidity, borrowing, utilization, and interest rates across AAVE V3 Ethereum market using live protocol data

## What I've Found
stablecoins dominate borrowing, while liquid staking tokens dominate supply but sit idle near 0% utilization.
WETH at 83.7% utilization with $4.7B borrowed, I've found people are depositing their ETH and using the WETH they receive and loop the rewards
Denominator-lesson: at first, mUSD looked huge until you check the supply and it's only 22k
Overall, The AAVE market is dominated and centered around Ether
## How it works
1.`fetch_data.py` — pulls live reserve data from the Aave v3 GraphQL API,
   cleans it (skips reserves with missing data), saves to CSV.
2. `analyze.py` — loads the CSV, computes utilization, filters out stablecoins
   and tiny markets, ranks what's left.
## How to run it
The commands: pip install ..., python fetch_data.py, python analyze.py

## What I learned
ETL pipelines, boolean filtering in pandas, reading tracebacks,
 why you never trust a ratio without its denominator

## Next steps
The interest-rate, time series
