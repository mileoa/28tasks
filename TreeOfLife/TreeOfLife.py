def make_older(tree: list[list[int]]) -> list[list[int]]:
    """Return tree with branches one year older."""
    for i, row in enumerate(tree):
        for j, el in enumerate(row):
            if el == 0:
                continue
            tree[i][j] += 1

    return tree

def fill_empty(tree: list[list[int]]) -> list[list[int]]:
    """Return tree with filled empty places by 1 year branches."""
    for i, row in enumerate(tree):
        for j, el in enumerate(row):
            if el != 0:
                continue
            tree[i][j] = 1

    return tree

def destroy_arround(tree: list[list[int]]) -> list[list[int]]:
    """Return tree with destroyd old branches and branches around."""
    to_be_destroyed: list[tuple[int, int]] = []
    for i, row in enumerate(tree):
        for j, el in enumerate(row):
            if el < 3:
                continue
            to_be_destroyed.append((i, j))
            if i-1 >= 0:
                to_be_destroyed.append((i-1, j))
            if i+1 <= len(tree)-1:
                to_be_destroyed.append((i+1, j))
            if j-1 >= 0:
                to_be_destroyed.append((i, j-1))
            if j+1 <= len(tree[0])-1:
                to_be_destroyed.append((i, j+1))

    for i, j in to_be_destroyed:
        tree[i][j] = 0

    return tree

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
    # Store years of branches.
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
        make_older(result_years)
        if i % 2 == 0:
            fill_empty(result_years)
            continue
        destroy_arround(result_years)

    return render(result_years)



