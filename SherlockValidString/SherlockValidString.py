def count_chars(s: str) -> dict[str, int]:
    """Return amount of each char in form of dict."""
    result: dict[str, int] = {}
    for i in s:
        if i not in result:
            result[i] = 0
            continue
        result[i] += 1

    return result


def SherlockValidString(s: str) -> bool:
    """Return whether is password valid."""
    if len(set(count_chars(s).values())) == 1:
        return True
    for i in range(len(s)):
        # Current char meets exact one time in string except itself position.
        if len(set(count_chars(s[:i] + s[i + 1 :]).values())) == 1:
            return True

    return False
