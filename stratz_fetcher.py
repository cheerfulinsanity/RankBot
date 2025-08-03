import requests

STRATZ_API_URL = "https://api.stratz.com/graphql"
HEADERS = {
    "authority": "api.stratz.com",
    "origin": "https://stratz.com",
    "referer": "https://stratz.com/",
    "user-agent": "Mozilla/5.0",
}

UNRANKED_MODES = {
    "ALL_PICK", "TURBO", "ABILITY_DRAFT", "ALL_RANDOM", "SINGLE_DRAFT",
    "LEAST_PLAYED", "ALL_RANDOM_DEATH_MATCH", "MID_ONLY", "CUSTOM"
}

BASE_QUERY = """
query getRecentMatches($steamId: Long!, $offset: Int!) {
  player(steamAccountId: $steamId) {
    matches(request: {
      take: 100,
      offset: $offset,
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
    all_matches = []

    for offset in [0, 100]:
        response = requests.post(
            STRATZ_API_URL,
            json={
                "query": BASE_QUERY,
                "variables": {"steamId": steam_id, "offset": offset}
            },
            headers=HEADERS
        )
        response.raise_for_status()
        data = response.json()

        matches = (
            data.get("data", {})
            .get("player", {})
            .get("matches", [])
        )

        # Filter to unranked only
        unranked = [m for m in matches if m.get("gameMode") in UNRANKED_MODES]
        all_matches.extend(unranked)

    return all_matches
