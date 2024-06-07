def odometer(oksana: list[int]) -> int:
    last_t: int = 0
    s: int = 0
    for i in range(1, len(oksana), 2):
        s += oksana[i-1] * (oksana[i] - last_t)
        last_t = oksana[i]
    return s


