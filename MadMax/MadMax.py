def MadMax(N: int, Tele: list[int]) -> list[int]:
    tele_copy = Tele.copy()

    center_el_index: int = N // 2
    tele_copy.sort()
    tele_right = tele_copy[center_el_index:]
    tele_right.sort(reverse=True)
    tele_copy[center_el_index:] = tele_right

    return tele_copy
