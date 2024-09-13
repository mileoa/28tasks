def generate_polygon(N: int, M: int) -> list[list[bool]]:
    result: list[list[bool]] = []
    for i in range(N):
        row: list[bool] = []
        for j in range(M):
            row.append(False)
        result.append(row)
    return result


def fill_polygon_soliders(
    polygon: list[list[bool]], L: int, battalion: list[int]
) -> list[list[bool]]:
    for i in range(0, L * 2, 2):
        # Use -1 because polygon has coordinates 1 ... N, 1 ... M
        polygon[battalion[i] - 1][battalion[i + 1] - 1] = True
    return polygon


def conquer_surrounding_cells(polygon: list[list[bool]]) -> list[list[bool]]:
    result: list[int] = []
    L: int = 0

    for i, cell_row in enumerate(polygon, 1):
        for j, cell in enumerate(cell_row, 1):
            if not cell:
                continue
            # Check out of bounds.
            if i - 1 >= 1:
                result.append(i - 1)
                result.append(j)
                L += 1
            # Check out of bounds.
            if i + 1 <= len(polygon):
                result.append(i + 1)
                result.append(j)
                L += 1
            # Check out of bounds.
            if j - 1 >= 1:
                result.append(i)
                result.append(j - 1)
                L += 1
            # Check out of bounds.
            if j + 1 <= len(polygon[0]):
                result.append(i)
                result.append(j + 1)
                L += 1

    polygon = fill_polygon_soliders(polygon, L, result)
    return polygon


def is_conquested(polygon: list[list[bool]]) -> bool:
    for row in polygon:
        for cell in row:
            if not cell:
                return False
    return True


def ConquestCampaign(N: int, M: int, L: int, battalion: list[int]) -> int:
    """
    Simulate conquest and return amount of needed days.

    N - amount of rows.
    M - amount of columns.
    L - amount of first conquested areas.
    battalion - pairs of coordinates of first conquested areas.
    battalion even indexes - N coordinate.
    battalion odd indexes - M coordinate.
    """
    polygon: list[list[bool]] = generate_polygon(N, M)
    polygon = fill_polygon_soliders(polygon, L, battalion)

    day: int = 1
    while not is_conquested(polygon):
        polygon = conquer_surrounding_cells(polygon)
        day += 1

    return day
