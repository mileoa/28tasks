def MisterRobot(N: int, data: list[int]) -> bool:
    """Return whether can sort by shifitng groups of 3 elements."""
    sorted_data: list[int] = [i+1 for i in range(N)]
    i: int = 0
    repeated_list: list[list[int]] = []

    # Try to sort until sucsess or repeat.
    while data != sorted_data:
        if i > len(data)-1-2:
            i = 0
        if data[i] < data[i+1] and data[i+1] < data[i+2]:
            i += 1
            continue

        for j in range(2):
            data[i], data[i+1], data[i+2] = data[i+1], data[i+2], data[i]

            # If begin to repeat than can't sort.
            if data in repeated_list:
                return False
            repeated_list.append(data[:])

            if data[i] < data[i+1] and data[i+1] < data[i+2]:
                break

        i += 1

    return True




