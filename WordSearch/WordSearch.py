def have_word(string: str, word: str) -> bool:
    for i in string.split(" "):
        if i == word:
            return True
    return False


def separate_word(word: str, lenght: int) -> list[str]:
    word_separeted_by_lines: list[str] = []
    for i in range(len(word) // lenght):
        word_separeted_by_lines.append(word[lenght * i : lenght * (i + 1)])
    if len(word) % lenght != 0:
        word_separeted_by_lines.append(word[len(word) - len(word) % lenght :])

    return word_separeted_by_lines


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
    for word in words:
        lines = add_to_line(len, word, lines)
    words = None

    word_lines_appearense: list[int] = []
    for line in lines:
        if have_word(line, subs):
            word_lines_appearense.append(1)
            continue
        word_lines_appearense.append(0)

    return word_lines_appearense
