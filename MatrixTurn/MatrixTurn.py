def circle_to_row(Matrix: list[str], M: int, N: int, circle_num: int) -> list[str]:
    """Return nth circle converted to row."""
    result: list[str] = []
    result += get_top_row_of_circle(Matrix, M, N, circle_num)
    result += get_right_column_of_circle(Matrix, M, N, circle_num)[1:-1]
    result += list(reversed(get_bottom_row_of_circle(Matrix, M, N, circle_num)))
    result += list(reversed(get_left_column_of_circle(Matrix, M, N, circle_num)))[1:-1]

    return result


def get_top_row_of_circle(
    Matrix: list[str], M: int, N: int, circle_num: int
) -> list[str]:
    """
    Return horizontal top row left to right.
    """
    horizontal_top_row: list[str] = []

    from_column: int = circle_num
    to_column: int = N - circle_num
    for i in range(from_column, to_column):
        horizontal_top_row.append(Matrix[circle_num][i])

    return horizontal_top_row


def get_right_column_of_circle(
    Matrix: list[str], M: int, N: int, circle_num: int
) -> list[str]:
    """
    Return right column of circle.
    """
    rgiht_column: list[str] = []
    from_row: int = circle_num
    to_row: int = M - circle_num
    for i in range(from_row, to_row):
        rgiht_column.append(Matrix[i][N - 1 - circle_num])
    return rgiht_column


def get_bottom_row_of_circle(
    Matrix: list[str], M: int, N: int, circle_num: int
) -> list[str]:
    """
    Return bottom row of circle.

    Circle_num is offset.
    """
    bottom_row: list[str] = []
    from_column = circle_num
    to_column = N - circle_num
    for i in range(from_column, to_column):
        bottom_row.append(Matrix[M - 1 - circle_num][i])
    return bottom_row


def get_left_column_of_circle(
    Matrix: list[str], M: int, N: int, circle_num: int
) -> list[str]:
    """
    Return left column of circle.

    Circle_num is offset.
    """
    left_column: list[str] = []
    # -1 not to be out of range.
    from_row = circle_num
    to_row = M - circle_num
    for i in range(from_row, to_row):
        left_column.append(Matrix[i][circle_num])
    return left_column


def shift_row(row: list[str]) -> list[str]:
    """Return row shifted right."""
    result: list[str] = row[-1:] + row[:-1]

    return result


def replace_circle_by_row(
    Matrix: list[str], M: int, N: int, row: list[str], circle_num: int
) -> None:
    """Replace nth circle by row."""
    row_i: int = 0

    # Process horizontal top row left to right.

    # circle_num is offset.
    from_column: int = circle_num
    to_column: int = N - circle_num
    for i in range(from_column, to_column):
        new_row: str = Matrix[circle_num][:i] + row[row_i] + Matrix[circle_num][i + 1 :]
        Matrix[circle_num] = new_row
        row_i += 1

    # Process vertical right column top down
    # except first and last elements.

    # circle_num is offset.
    from_row: int = circle_num + 1  # +1 to except first element.
    to_row: int = M - 1 - circle_num  # -1 to except last element.
    for i in range(from_row, to_row):
        new_row = (
            Matrix[i][: N - circle_num - 1] + row[row_i] + Matrix[i][N - circle_num :]
        )
        Matrix[i] = new_row
        row_i += 1

    # Process horisontal bottom row right to left.

    # circle_num is offset.
    from_column = N - 1 - circle_num  # -1 not to be out of range.
    to_column = circle_num - 1
    for i in range(from_column, to_column, -1):
        new_row = (
            Matrix[M - 1 - circle_num][:i]
            + row[row_i]
            + Matrix[M - 1 - circle_num][i + 1 :]
        )
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
        new_row = Matrix[i][:circle_num] + row[row_i] + Matrix[i][circle_num + 1 :]
        Matrix[i] = new_row
        row_i += 1

    return None


def MatrixTurn(Matrix: list[str], M: int, N: int, T: int) -> None:
    """
    Return Matrix rotated around center T times.

    M - amount of rows.
    N - amount of columns.
    """
    circles_amount: int = int(min(M, N) / 2)
    rows: list[list[str]] = []

    for i in range(circles_amount):
        rows.append(circle_to_row(Matrix, M, N, i))

    for i in range(T):
        for j in range(circles_amount):
            rows[j] = shift_row(rows[j])

    for i in range(circles_amount):
        replace_circle_by_row(Matrix, M, N, rows[i], i)

    return None
