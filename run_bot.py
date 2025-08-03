from stratz_fetcher import fetch_recent_matches
from filter_logic import extract_solo_unranked_ranks
from rank_analyzer import compute_average_rank

def run(steam_ids):
    for sid in steam_ids:
        print(f"Checking {sid}...")
        try:
            raw = fetch_recent_matches(sid)
            matches = extract_solo_unranked_ranks(raw, sid)
            avg_rank = compute_average_rank(matches)
            print(f"Player {sid}: {len(matches)} solo unranked matches. Avg rank: {avg_rank}")
        except Exception as e:
            print(f"Failed for {sid}: {e}")

if __name__ == "__main__":
    steam_id_list = [84228471, 116031702]
    run(steam_id_list)
