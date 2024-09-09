def remove_chars(s: str, char: str) -> str:
    """Remove given char from string."""
    result: list[str] = []
    for i in s:
        if i != char:
            result.append(i)
    return "".join(result)


def calculate_encode_rows_amount(srting_lenght: int, columns_amount: int) -> int:
    """
    Return calculated rows amount.
    """
    rows_amount: int = int((srting_lenght**0.5))
    while rows_amount * columns_amount < srting_lenght:
        rows_amount += 1
    return rows_amount


def calculate_encode_columns_amount(srting_lenght: int) -> int:
    """
    Return calculated columns amount.
    """
    return int(srting_lenght**0.5) + 1


def get_normilized_string(string: str, rows_amount: int, columns_amount: int) -> str:
    """
    Return normilized string with appended spaces to string lenght
    equel matrix elements amount.
    """
    normilized_string: str = string
    while len(normilized_string) < rows_amount * columns_amount:
        normilized_string += " "
    return normilized_string


def make_encode_matrix(s: str) -> list[list[str]]:
    """Make cipher matrix from string.

    Make chipher matrix from string with removed spaces.
    Reuslt matrix additionaly has " " as elements
    if string chars does not fills all matrix position.
    """
    columns_amount: int = calculate_encode_columns_amount(len(s))
    rows_amount: int = calculate_encode_rows_amount(len(s), columns_amount)
    normilized_s: str = get_normilized_string(s, rows_amount, columns_amount)
    matrix: list[list[str]] = []
    for i in range(rows_amount):
        row: list[str] = []
        for j in range(columns_amount):
            row.append(normilized_s[i * rows_amount + j])
        matrix.append(row)

    return matrix


def make_decode_matrix(s: str) -> list[list[str]]:
    """Make decode matix.

    Make matrix from encrypted string.
    Last matrix column may contain additional " " as elements
    to fill empty elements.
    """
    result: list[list[str]] = []
    columns_amount: int = int(len(remove_chars(s, " ")) ** 0.5) + 1
    for i in s.split(" "):
        result.append(list(i))
        while len(result[-1]) != columns_amount:
            result[-1].append(" ")
    columns_amount = -1

    return result


def get_transposed_matrix(matrix: list[list[str]]) -> list[list[str]]:
    """Transpose matrix."""
    result: list[list[str]] = []
    for i in range(len(matrix[0])):
        result.append([])

    for i in range(len(matrix[0])):
        for sub_list in matrix:
            result[i].append(sub_list[i])

    return result


def TheRabbitsFoot(s: str, encode: bool) -> str:
    """Encode or decode string with "red suitcase" cipher."""
    matrix: list[list[str]] = []
    if encode:
        space_removed: str = remove_chars(s, " ")
        matrix = make_encode_matrix(space_removed)
    else:
        matrix = make_decode_matrix(s)

    result: list[str] = []
    for i in get_transposed_matrix(matrix):
        for j in i:
            if j != " ":
                result.append(j)
        if encode:
            result.append(" ")
    while result[-1] == " ":
        result.pop()  # Delete last space.

    return "".join(result)
