def remove_chars(s: str, char: str) -> str:
    result: list[str] = []
    for i in s:
        if i != char:
            result.append(i)
    return "".join(result)

def make_matrix(s: str) -> list[list[str]]:
    lenght: int = len(s)
    rows: int = int((lenght**0.5))
    columns: int = int(lenght**0.5) + 1

    while rows * columns < lenght:
        rows += 1

    while len(s) < rows * columns:
        s += " "

    matrix: list[list[str]] = []
    char_i: int = 0

    for i in range(rows):
        row: list[str] = []
        for j in range(columns):
            row.append(s[char_i])
            char_i += 1
        matrix.append(row)

    return matrix

def make_decode_matrix(s: str) -> list[list[str]]:
    result: list[list[str]] = []

    columns: int = int(len(remove_chars(s, " "))**0.5) + 1

    for i in s.split(" "):
        result.append(list(i))
        while len(result[-1]) != columns:
            result[-1].append(" ")

    return result


def trans_matrix(matrix: list[list[str]]) -> list[list[str]]:

    result: list[list[str]] = []
    for i in range(len(matrix[0])):
        result.append([])

    for i in range(len(matrix[0])):
        for sub_list in matrix:
            result[i].append(sub_list[i])

    return result

def TheRabbitsFoot(s: str, encode: bool) -> str:

    matrix: list[list[str]] = []
    if encode:
        space_removed: str = remove_chars(s, " ")
        matrix = make_matrix(space_removed)
    else:
        matrix = make_decode_matrix(s)

    t_matrix: list[list[str]] = trans_matrix(matrix)

    result: list[str] = []
    for i in t_matrix:
        for j in i:
            if j != " ":
                result.append(j)
        if encode:
            result.append(" ")
    while result[-1] == " ":
        result.pop() # Delete last space.

    return "".join(result)




