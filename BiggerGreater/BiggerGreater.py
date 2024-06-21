def get_next_greater_char_index(start: int, string: list[str], char: str) -> int:
    """Return index of next greater char."""
    for i in range(start, len(string)):
        if i == start:
            index: int = i
            continue
        if string[i] < string[index] and string[i] > char:
            index = i

    return index

def count_greater_chars(start:int, chars: list[str], char: str) -> int:
    """Return amount of forward unique chars greater than given char."""
    result: int = 0
    for i in set(chars[start:]):
        if i > char:
            result += 1

    return result

def sort_swap(chars: list[str]) -> list[str]:
    """Sort list asc by swaping 2 elements."""
    result: list[str] = chars[:]
    xchange = True

    while xchange:
        xchange = False
        for i in range(len(result) - 1):
            if result[i] > result[i+1]:
                result[i], result[i+1] = result[i+1], result[i]
                xchange = True
    return result

def BiggerGreater(input: str) -> str:
    """Return magic word or empty string."""
    result_chars: list[str] = list(input)

    # Try to find element after which there is bigger
    # elements. So we can switch elements in most
    # optimal way.
    first_change_made: bool = False
    for i in range(len(result_chars)-1, -1, -1):
        second_start: int = i + 1
        if count_greater_chars(i, result_chars, result_chars[i]) > 0:
            char_index: int = get_next_greater_char_index(i+1, result_chars, result_chars[i])
            result_chars[char_index], result_chars[i] = result_chars[i], result_chars[char_index]
            first_change_made = True
            break

    if not first_change_made:
        return ""

    # Now can sort elements in asc order to get
    # the smallest possible string.
    result_chars = result_chars[:second_start] + sort_swap(result_chars[second_start:])

    return "".join(result_chars)




