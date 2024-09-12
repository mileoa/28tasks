def Unmanned(L: int, N: int, track: list[list[int]]) -> int:
    # Light position to light cilces.
    light_cicle: dict[int, list[int]] = {}
    for light in track:
        light_cicle[light[0]] = [light[1], light[2]]

    vehicle_pos: int = 0
    time_spent: int = 0
    while vehicle_pos < L:
        is_red_light_on_vehicle_postition: bool = False
        is_vehicle_on_the_light: bool = vehicle_pos in light_cicle
        if is_vehicle_on_the_light:
            is_red_light_on_vehicle_postition: bool = (
                time_spent % sum(light_cicle[vehicle_pos]) < light_cicle[vehicle_pos][0]
            )
        if is_red_light_on_vehicle_postition:
            time_spent += 1
            continue

        vehicle_pos += 1
        time_spent += 1

    return time_spent
