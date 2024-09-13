def MadMax(N: int, Tele: list[int]) -> list[int]:
    """
    Return list with max element in the center. Left side
    of the list are asc sorted and right side elements are desc sorted.
    """
    tele_copy = Tele.copy()

    center_el_index: int = N // 2
    tele_copy.sort()
    tele_right = tele_copy[center_el_index:]
    tele_right.sort(reverse=True)
    tele_copy[center_el_index:] = tele_right

    return tele_copy
