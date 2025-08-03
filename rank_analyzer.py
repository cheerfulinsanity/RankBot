def compute_average_rank(match_list):
    if not match_list:
        return None
    return sum(m["rank"] for m in match_list) / len(match_list)
