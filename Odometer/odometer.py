def odometer(oksana: list[int]) -> int:
    hours_passed_from_start: int = 0
    path_lenght_km: int = 0
    for i in range(1, len(oksana), 2):
        path_lenght_km += oksana[i - 1] * (oksana[i] - hours_passed_from_start)
        hours_passed_from_start = oksana[i]
    return path_lenght_km
