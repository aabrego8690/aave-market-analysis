import requests

url = "https://api.v3.aave.com/graphql"

query = """
{
  market(request: {
    address: "0x87870bca3f3fd6335c3f4ce8392d69350b4fa4e2",
    chainId: 1
  }) {
    name
    reserves {
      underlyingToken { symbol address }
      size { usd }
      borrowInfo {
        total { usd }
        availableLiquidity { usd }
      }
    }
  }
}
"""

response = requests.post(
    url,
    json={"query": query},
    timeout=30
)
response.raise_for_status()

payload = response.json()
print(payload["data"]["market"]["name"])