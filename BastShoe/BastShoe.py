# TODO rewrite logic with using of class
string: str = ""
do_list: list[str] = [""]
i_do_list: int = 0


def should_clear_do_list() -> bool:
    """Return whether should clear do list."""
    global do_list
    global i_do_list

    if i_do_list < len(do_list) - 1:
        return True
    return False


def clear_do_list() -> None:
    """Make do list empty."""
    global do_list
    global i_do_list

    do_list = []
    i_do_list = -1

    return None


def add_do_list(S: str) -> None:
    """Add to do list history."""
    global do_list
    global i_do_list

    do_list.append(S)
    i_do_list += 1


def add(S: str) -> str:
    """Add to end of the string."""
    global string

    if should_clear_do_list():
        clear_do_list()
        add_do_list(string)

    string = string + S
    add_do_list(string)

    return string


def delete(N: int) -> str:
    """Delete last N chars."""
    global string

    if should_clear_do_list():
        clear_do_list()
        add_do_list(string)

    string = string[: len(string) - N]
    add_do_list(string)

    return string


def give(i: int) -> str:
    """Return i el of string or empty string if out of range."""
    if i < 0 or i >= len(string):
        return ""
    return string[i]


def Undo() -> str:
    """Undo last changes."""
    global string
    global do_list
    global i_do_list

    if i_do_list - 1 >= 0:
        i_do_list -= 1
        string = do_list[i_do_list]

    return string


def Redo() -> str:
    """Redo last undo."""
    global string
    global do_list
    global i_do_list

    if i_do_list + 1 < len(do_list):
        i_do_list += 1
        string = do_list[i_do_list]

    return string


def BastShoe(command: str) -> str:
    """Return result of wanted proccess."""
    result: str = string

    if len(command) == 0:
        return result

    match command[0]:
        case "1":
            if len(command) > 2:
                result = add(command[2:])
        case "2":
            if len(command) > 2:
                try:
                    result = delete(int(command[2:]))
                except Exception:
                    pass
        case "3":
            if len(command) > 2:
                try:
                    result = give(int(command[2:]))
                except Exception:
                    pass
        case "4":
            if len(command) == 1:
                result = Undo()
        case "5":
            if len(command) == 1:
                result = Redo()

    return result
