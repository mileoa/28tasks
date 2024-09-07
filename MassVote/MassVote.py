def MassVote(N: int, Votes: list[int]) -> str:
    """Return vote result."""
    total_votes: int = sum(Votes)

    percents_of_votes_for_candidates: dict[int, float] = {}
    for i in range(N):
        percents_of_votes_for_candidates[i + 1] = (
            round(Votes[i] / total_votes, 3) * 100.0
        )

    percent_values: list[float] = list(percents_of_votes_for_candidates.values())
    max_percent: float = max(percent_values)
    if percent_values.count(max_percent) > 1:
        return "no winner"

    result_text: str = ""
    if max_percent > 50:
        result_text = "majority winner "
    else:
        result_text = "minority winner "

    for i, percent in percents_of_votes_for_candidates.items():
        if percent == max_percent:
            return result_text + str(i)

    return "no winner"
