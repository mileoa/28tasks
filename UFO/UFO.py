OCTAL_BASE = 8
HEXADECIMAL_BASE = 16


def list_int(num: int) -> list[int]:
    """List int by digits."""
    result: list[int] = []
    while num > 0:
        result.append(num % 10)
        num = num // 10
    result.reverse()
    return result


def convert_to_dec(num: int, base: int) -> int:
    """Convert to decimical."""
    digits: list[int] = list_int(num)
    result: int = 0
    for i, digit in enumerate(digits):
        result += digit * base ** (len(digits) - 1 - i)
    return result


def UFO(N: int, data: list[int], octal: bool) -> list[int]:
    """Return converted UFO sygnal."""
    base: int = 0
    if octal:
        base = OCTAL_BASE
    else:
        base = HEXADECIMAL_BASE

    result: list[int] = []
    for i in range(N):
        result.append(convert_to_dec(data[i], base))
    return result
