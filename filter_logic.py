def is_solo_match(match, steam_id):
    player_party = None
    party_counts = {}

    for player in match["players"]:
        pid = player.get("partyId")
        sid = player.get("steamAccountId")
        if sid == steam_id:
            player_party = pid
        party_counts[pid] = party_counts.get(pid, 0) + 1

    return player_party is not None and party_counts[player_party] == 1

def is_unranked_game(game_mode):
    return game_mode in {
        "ALL_PICK", "TURBO", "SINGLE_DRAFT", "RANDOM_DRAFT",
        "ALL_RANDOM", "ABILITY_DRAFT", "LEAST_PLAYED", "MID_ONLY"
    }

def extract_solo_unranked_ranks(data, steam_id):
    matches = data["data"]["player"]["matches"]
    solo_unranked = []

    for match in matches:
        if is_solo_match(match, steam_id) and is_unranked_game(match["gameMode"]):
            solo_unranked.append({
                "matchId": match["id"],
                "rank": match["rank"],
                "mode": match["gameMode"],
                "timestamp": match["startDateTime"]
            })

    return solo_unranked
