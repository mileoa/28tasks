NEEDED_ENEMIES_AMOUNT = 3
DIGITS_SUM_TO_DO_SEARCH = 10
ASCII_CODE_OF_CHAR_1 = 49
ASCII_CODE_OF_CHAR_9 = 57
ENEMY_SYMBOL = "="


def white_walkers(village: str) -> bool:
    """Return whether there are enemies."""
    found_valid_pair: bool = False
    for i, el_i in enumerate(village):
        if ord(el_i) < ASCII_CODE_OF_CHAR_1 or ord(el_i) > ASCII_CODE_OF_CHAR_9:
            continue
        enemies_count: int = 0
        for j in range(i + 1, len(village)):
            el_j: str = village[j]
            if el_j == ENEMY_SYMBOL:
                enemies_count += 1
                continue
            if ord(el_j) < ASCII_CODE_OF_CHAR_1 or ord(el_j) > ASCII_CODE_OF_CHAR_9:
                continue
            if int(el_i) + int(el_j) != DIGITS_SUM_TO_DO_SEARCH:
                continue
            if enemies_count < NEEDED_ENEMIES_AMOUNT:
                return False
            found_valid_pair = True

    return found_valid_pair
