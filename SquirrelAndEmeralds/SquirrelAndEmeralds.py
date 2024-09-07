def factorial(N: int) -> int:
    result: int = 1
    for i in range(2, N + 1):
        result *= i
    return result


def get_first_digit(num: int) -> int:
    while num >= 10:
        num = num // 10
    return num


def squirrel(N: int) -> int:
    return get_first_digit(factorial(N))
