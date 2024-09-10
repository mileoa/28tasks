from collections import deque


def odometer(oksana: list[int]) -> int:
    oksana_deque: deque[int] = deque(oksana)
    hours_passed_from_start: int = 0
    path_lenght_km: int = 0
    while len(oksana_deque) != 0:
        average_speed_from_last_point_kmph: int = oksana_deque.popleft()
        hours_passed_from_start_new: int = oksana_deque.popleft()
        path_lenght_km += average_speed_from_last_point_kmph * (
            hours_passed_from_start_new - hours_passed_from_start
        )
        hours_passed_from_start = hours_passed_from_start_new
    return path_lenght_km
