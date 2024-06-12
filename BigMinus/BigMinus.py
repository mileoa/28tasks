def is_more(s1: str, s2: str) -> bool:
    """Return whether int in s1 string more than int in s2."""
    for i, s1_digit in enumerate(s1):
        if s2[i] < s1_digit:
            return True
        if s2[i] > s1_digit:
            return False
    return False

def BigMinus(s1: str, s2: str) -> str:
    """Return absolute difference."""
    # Add leading 0 to make str equal len.
    while len(s1) > len(s2):
        s2 = "0"+ s2
    while len(s1) < len(s2):
        s1 = "0"+ s1

    # Decide minuend and subtrahend.
    result: list[str] = []
    subtrahend: str = ""

    if is_more(s1, s2):
        result = list(s1)
        subtrahend = s2
    else:
        result = list(s2)
        subtrahend = s1

    # School arithmetic.
    for i in range(len(result)-1, -1, -1):

        if int(result[i]) - int(subtrahend[i]) < 0:
            result[i - 1] = str(int(result[i - 1]) - 1)
            result[i] = str(int(result[i]) + 10 - int(subtrahend[i]))
            continue
        result[i] = str(int(result[i]) - int(subtrahend[i]))

    # Remove leading zeros.
    while result[0] == "0" and len(result) > 1:
        del result[0]

    return "".join(result)




