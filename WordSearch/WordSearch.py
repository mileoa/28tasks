def have_word(string: str, word: str) -> bool:
    for i in string.split(" "):
        if i == word:
            return True
    return False


def separate_word(word: str, lenght: int) -> list[str]:
    result: list[str] = []
    for i in range(len(word) // lenght):
        result.append(word[lenght * i : lenght * (i + 1)])
    if len(word) % lenght != 0:
        result.append(word[len(word) - len(word) % lenght :])

    return result


def add_to_line(lenght: int, word: str, lines: list[str]) -> list[str]:
    current_line: int = len(lines) - 1

    is_current_line_empty: bool = lines[current_line] == ""
    is_insertion_to_empty_line: bool = is_current_line_empty and len(word) <= lenght
    is_word_must_be_transfered: bool = is_current_line_empty and len(word) > lenght
    is_insertion_to_filled_line_without_transfer: bool = (
        len(lines[current_line]) + 1 + len(word) <= lenght
    )

    if is_insertion_to_empty_line:
        lines[current_line] += word
    elif is_word_must_be_transfered:
        for sep_word in separate_word(word, lenght):
            lines = add_to_line(lenght, sep_word, lines)
    elif is_insertion_to_filled_line_without_transfer:
        lines[current_line] += " " + word
    else:
        lines.append("")
        lines = add_to_line(lenght, word, lines)

    return lines


def WordSearch(len: int, s: str, subs: str) -> list[int]:
    words: list[str] = s.split(" ")
    lines: list[str] = [""]
    result: list[int] = []
    for word in words:
        lines = add_to_line(len, word, lines)

    for line in lines:
        if have_word(line, subs):
            result.append(1)
            continue
        result.append(0)

    return result
