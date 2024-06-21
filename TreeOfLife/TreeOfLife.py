def make_older(tree: list[list[int]]) -> list[list[int]]:
    """Return tree with branches one year older."""
    result: list[list[int]] = tree[:]
    for i, row in enumerate(tree):
        for j, el in enumerate(row):
            if el == 0:
                continue
            result[i][j] += 1

    return result

def fill_empty(tree: list[list[int]]) -> list[list[int]]:
    """Return tree with filled empty places by 1 year branches."""
    result: list[list[int]] = tree[:]
    for i, row in enumerate(tree):
        for j, el in enumerate(row):
            if el != 0:
                continue
            result[i][j] = 1

    return result

def destroy_arround(tree: list[list[int]]) -> list[list[int]]:
    """Return tree with destroyd old branches and branches around."""
    result: list[list[int]] = tree[:]
    for i, row in enumerate(tree):
        for j, el in enumerate(row):
            if el < 3:
                continue
            result[i][j] = 0
            if i-1 >= 0:
                result[i-1][j] = 0
            if i+1 <= len(tree)-1:
                result[i+1][j] = 0
            if j-1 >= 0:
                result[i][j-1] = 0
            if j+1 <= len(tree[0])-1:
                result[i][j+1] = 0

    return result

def render(years: list[list[int]]) -> list[str]:
    """Return rendered tree."""
    result: list[str] = []
    for row in years:
        result_row: list[str] = []
        for el in row:
            if el == 0:
                result_row.append(".")
                continue
            result_row.append("+")
        result.append("".join(result_row))

    return result


def TreeOfLife(H: int, W: int, N: int, tree: list[str]) -> list[str]:
    """Return simulated tree growth for N years."""
    result_rendered: list[str] = tree[:]
    result_years: list[list[int]] = []
    for row in tree:
        result_row: list[int] = []
        for el in row:
            if el == ".":
                result_row.append(0)
                continue
            result_row.append(1)
        result_years.append(result_row)


    for i in range(N):
        result_years = make_older(result_years)
        if i % 2 == 0:
            result_years = fill_empty(result_years)
        else:
            result_years = destroy_arround(result_years)
        result_rendered = render(result_years)

    return result_rendered



