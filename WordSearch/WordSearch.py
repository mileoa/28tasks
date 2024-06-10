def have_word(string: str, word: str) -> bool:
    for i in string.split(" "):
        if i == word:
            return True
    return False

def separate_word(word: str, lenght: int) -> list[str]:
    result: list[str] = []
    for i in range(len(word)//lenght):
        result.append(word[lenght*i:lenght*(i+1)])
    if len(word)%lenght != 0:
        result.append(word[len(word) - len(word)%lenght :])

    return result


def add_to_line(lenght: int, word: str, lines: list[str]) -> list[str]:
    current_line: int = len(lines) - 1

    if lines[current_line] == "" and len(word) <= lenght:
        lines[current_line] += word
    elif lines[current_line] == "" and len(word) > lenght:
        for sep_word in separate_word(word, lenght):
            lines = add_to_line(lenght, sep_word, lines)
    elif len(lines[current_line]) + 1 + len(word) <= lenght:
        lines[current_line] += " " + word
    elif len(lines[current_line]) + 1 + len(word) > lenght:
        lines.append("")
        lines = add_to_line(lenght, word, lines)

    return lines


def WordSearch(len: int, s: str, subs: str) -> list[int]:
    words: list[str] = s.split(" ")
    lines: list[str] = [""]
    result: list[int] = []
    for word in words:
        lines = add_to_line(len, word, lines)

    for i, line in enumerate(lines):
        if have_word(line, subs):
            result.append(1)
            continue
        result.append(0)

    return result
