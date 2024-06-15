def LineAnalysis(line: str) -> bool:
    """Return whether pattern vaild."""
    # Find common pattern except firest char of pattern.
    commom_pattern: str = ""

    for i in range(1, len(line)):
        commom_pattern += line[i]
        if line[i] == "*":
            break

    for i in range(1, len(line)):
        pattern_offset: int = i%len(commom_pattern) - 1
        if commom_pattern[pattern_offset] != line[i]:
            return False

    return True



