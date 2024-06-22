def circle_to_row(Matrix: list[str], M: int, N: int, circle_num: int) -> list[str]:
    """Return nth circle converted to row."""
    result: list[str] = []

    # Process horizontal top row left to right.

    from_column: int = circle_num
    to_column: int = N - circle_num
    for i in range(from_column, to_column):
        result.append(Matrix[circle_num][i])

    # Process vertical right column top down
    # except first and last elements.

    from_row: int = circle_num + 1 # +1 to except first element.
    to_row: int = M - 1 - circle_num # -1 to except last element.
    for i in range(from_row, to_row):
        result.append(Matrix[i][N - 1 - circle_num])

    # Process horisontal bottom row right to left.

    # circle_num is offset.
    from_column = N - 1 - circle_num # -1 not to be out of range.
    to_column = circle_num - 1
    for i in range(from_column, to_column, -1):
        result.append(Matrix[M - 1 - circle_num][i])

    # Process vertical left column down up
    # except first and last elements.

    # circle_num is offset.
    # -1 not to be out of range.
    # -1 to except first element.
    from_row = M - 1 - 1 - circle_num
    to_row = circle_num
    for i in range(from_row, to_row, -1):
        result.append(Matrix[i][circle_num])

    return result

def shift_row(row: list[str]) -> list[str]:
    """Return row shifted right."""
    result: list[str] = row[-1:] + row[:-1]

    return result

def replace_circle_by_row(Matrix: list[str], M: int, N: int, row: list[str], circle_num: int) -> None:
    """Replace nth circle by row."""
    row_i: int = 0

    # Process horizontal top row left to right.

    # circle_num is offset.
    from_column: int = circle_num
    to_column: int = N - circle_num
    for i in range(from_column, to_column):
        new_row: str = Matrix[circle_num][:i] + row[row_i] + Matrix[circle_num][i+1:]
        Matrix[circle_num] = new_row
        row_i += 1

    # Process vertical right column top down
    # except first and last elements.

    # circle_num is offset.
    from_row: int = circle_num + 1 # +1 to except first element.
    to_row: int = M - 1 - circle_num # -1 to except last element.
    for i in range(from_row, to_row):
        new_row = Matrix[i][:N - circle_num - 1] + row[row_i] + Matrix[i][N - circle_num:]
        Matrix[i] = new_row
        row_i += 1

    # Process horisontal bottom row right to left.

    # circle_num is offset.
    from_column = N - 1 - circle_num # -1 not to be out of range.
    to_column = circle_num - 1
    for i in range(from_column, to_column, -1):
        new_row = Matrix[M - 1 - circle_num][:i] + row[row_i] + Matrix[M - 1 - circle_num][i+1:]
        Matrix[M - 1 - circle_num] = new_row
        row_i += 1

    # Process vertical left column down up
    # except first and last elements.

    # circle_num is offset.
    # -1 not to be out of range.
    # -1 to except first element.
    from_row = M - 1 - 1 - circle_num
    to_row = circle_num
    for i in range(from_row, to_row, -1):
        new_row = Matrix[i][:circle_num] + row[row_i] + Matrix[i][circle_num + 1:]
        Matrix[i] = new_row
        row_i += 1

    return None


def MatrixTurn(Matrix: list[str], M: int, N: int, T: int) -> None:
    """Return Matrix rotated around center T times."""
    circles_amount: int = int(min(M, N)/2)
    rows: list[list[str]] = []

    for i in range(circles_amount):
        rows.append(circle_to_row(Matrix, M, N, i))

    for i in range(T):
        for j in range(circles_amount):
            rows[j] = shift_row(rows[j])

    for i in range(circles_amount):
        replace_circle_by_row(Matrix, M, N, rows[i], i)

    return None







