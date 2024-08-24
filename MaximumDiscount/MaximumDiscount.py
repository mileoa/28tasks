def MaximumDiscount(N: int, price: list[int]) -> int:
    """Return max discount."""
    return sum(
        sorted(price, reverse=True)[i] for i in range(len(price)) if (i + 1) % 3 == 0
    )
