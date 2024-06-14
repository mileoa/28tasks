def Unmanned(L: int, N: int, track: list[list[int]]) -> int:
    vehicle_pos: int = 0
    time_spent: int = 0

    # Light position to light cilces.
    light_cicle: dict[int, list[int]] = {}
    for light in track:
        light_cicle[light[0]] = [light[1], light[2]]

    while vehicle_pos < L:
        # Car on light and light is red.
        if (vehicle_pos in light_cicle and
            # Check what part of full cicle is.
            time_spent % sum(light_cicle[vehicle_pos]) < light_cicle[vehicle_pos][0]):
            time_spent += 1
            continue

        vehicle_pos += 1
        time_spent += 1

    return time_spent



