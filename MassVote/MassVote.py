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
    candidate_with_max_percent: str = str(
        list(percents_of_votes_for_candidates.keys())[
            list(percents_of_votes_for_candidates.values()).index(max_percent)
        ]
    )
    if max_percent > 50:
        return "majority winner " + candidate_with_max_percent
    return "minority winner " + candidate_with_max_percent
