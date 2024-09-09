def calculate_lenght_between_dots(a: int, b: int) -> float | int:

    if a == 6 and b in (5, 1):
        return 1
    if a == 1 and b in (6, 2, 9):
        return 1
    if a == 9 and b in (1, 8):
        return 1
    if a == 5 and b in (6, 4, 2):
        return 1
    if a == 2 and b in (1, 5, 3, 8):
        return 1
    if a == 8 and b in (9, 2, 7):
        return 1
    if a == 4 and b in (5, 3):
        return 1
    if a == 3 and b in (2, 4, 7):
        return 1
    if a == 7 and b in (8, 3):
        return 1
    return 2 ** (0.5)


def PatternUnlock(N: int, hits: list[int]) -> str:
    lenght: float = round(
        sum(calculate_lenght_between_dots(hits[i], hits[i + 1]) for i in range(N - 1)),
        5,
    )
    result: list[str] = []
    for el in str(lenght):
        if el not in ("0", "."):
            result.append(el)

    return "".join(result)
