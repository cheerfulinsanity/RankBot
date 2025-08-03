import requests

STRATZ_API_URL = "https://api.stratz.com/graphql"
HEADERS = {
    "authority": "api.stratz.com",
    "origin": "https://stratz.com",
    "referer": "https://stratz.com/",
    "user-agent": "Mozilla/5.0",
}

QUERY = """
query getRecentMatches($steamId: Long!) {
  player(steamAccountId: $steamId) {
    matches(request: {
      take: 100,
      isStats: true
    }) {
      id
      startDateTime
      gameMode
      rank
      players {
        steamAccountId
        partyId
      }
    }
  }
}
"""

def fetch_recent_matches(steam_id):
    response = requests.post(
        STRATZ_API_URL,
        json={"query": QUERY, "variables": {"steamId": steam_id}},
        headers=HEADERS
    )
    response.raise_for_status()
    return response.json()
