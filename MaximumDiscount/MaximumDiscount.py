def MaximumDiscount(N: int, price: list[int]) -> int:
    """Return max discount."""
    total_discount: int = 0

    sorted_price: list[int] = price[:]
    sorted_price.sort(reverse=True)

    for i in range(N//3):
        total_discount += sorted_price[i*3 + 2]

    return total_discount



