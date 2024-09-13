def swaped_el(F: list[int], i_1: int, i_2: int) -> list[int]:
    """Return new list with elements swaped on given indexes."""
    result: list[int] = F[:]
    result[i_1], result[i_2] = result[i_2], result[i_1]

    return result


def Football(F: list[int], N: int) -> bool:
    """Decide whether list can be ordered using one of two tricks."""
    sorted_F: list[int] = sorted(F)

    # Second trick.
    if list(reversed(F)) == sorted_F:
        return True

    # First trick.
    for i in range(N):
        for j in range(i + 1, N):
            if swaped_el(F, i, j) == sorted_F:
                return True

    return False
