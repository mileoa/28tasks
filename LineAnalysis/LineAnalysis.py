def get_common_pattern(line: str) -> str:
    """
    Return common pattern from given string.

    Common pattern is pattern between two "*" chars.
    """
    commom_pattern: str = ""
    for i in range(1, len(line)):
        commom_pattern += line[i]
        if line[i] == "*":
            break
    return commom_pattern


def LineAnalysis(line: str) -> bool:
    """Return whether pattern vaild."""
    commom_pattern: str = get_common_pattern(line)

    for i in range(1, len(line)):
        pattern_offset: int = i % len(commom_pattern) - 1
        if commom_pattern[pattern_offset] != line[i]:
            return False

    return True
