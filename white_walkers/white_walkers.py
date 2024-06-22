def white_walkers(village: str) -> bool:
    """Return whether there are enemies."""
    was_valid_pair: bool = False
    for i, el_i in enumerate(village):
        if ord(el_i) < 49 or ord(el_i) > 57:
            continue
        enemies_count: int = 0
        for j in range(i+1, len(village)):
            el_j: str = village[j]
            if el_j == "=":
                enemies_count += 1
                continue
            if ord(el_j) < 49 or ord(el_j) > 57:
                continue
            if int(el_i) + int(el_j) != 10:
                continue
            if enemies_count < 3:
                return False
            was_valid_pair = True

    return was_valid_pair





