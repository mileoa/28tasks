def is_more(s1: str, s2: str) -> bool:
    """Return whether int in s1 string more than int in s2."""
    for i, s1_digit in enumerate(s1):
        if s2[i] < s1_digit:
            return True
        if s2[i] > s1_digit:
            return False
    return False


def get_normilized_result(arr: list[str]) -> list[str]:
    normilized_result: list[str] = arr[:]
    while normilized_result[0] == "0" and len(normilized_result) > 1:
        del normilized_result[0]
    return normilized_result


def get_normilized_minuend_and_subtrahend(s1: str, s2: str) -> list[list[str], str]:
    """
    Return tuple (minuend, subtrahend)
    """
    normilized_s1: str = s1
    normilized_s2: str = s2
    while len(normilized_s1) > len(normilized_s2):
        normilized_s2: str = "0" + normilized_s2
    while len(normilized_s1) < len(normilized_s2):
        normilized_s1 = "0" + normilized_s1

    minuend: str = ""
    subtrahend: str = ""
    if is_more(normilized_s1, normilized_s2):
        minuend = list(normilized_s1)
        subtrahend = normilized_s2
    else:
        minuend = list(normilized_s2)
        subtrahend = normilized_s1
    return (minuend, subtrahend)


def BigMinus(s1: str, s2: str) -> str:
    """Return absolute difference."""
    minuend: list[str]
    subtrahend: str
    minuend, subtrahend = get_normilized_minuend_and_subtrahend(s1, s2)

    # School arithmetic.
    for i in range(len(minuend) - 1, -1, -1):

        if int(minuend[i]) - int(subtrahend[i]) < 0:
            minuend[i - 1] = str(int(minuend[i - 1]) - 1)
            minuend[i] = str(int(minuend[i]) + 10 - int(subtrahend[i]))
            continue
        minuend[i] = str(int(minuend[i]) - int(subtrahend[i]))

    return "".join(get_normilized_result(minuend))
