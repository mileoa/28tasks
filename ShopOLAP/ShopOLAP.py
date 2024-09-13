def sort_by_amount(item: str) -> int:
    """Return sold amount from item string."""
    return int(item.split()[1])


def sort_by_name(item: str) -> str:
    """Return item name from item string."""
    return item.split()[0]


def ShopOLAP(N: int, items: list[str]) -> list[str]:
    """Return grouped and sorted desc sold items and amount."""
    pre_result: list[str, int] = {}
    for item in items:
        item_name: str
        item_amount: str
        item_name, item_amount = item.split()
        if item_name in pre_result:
            pre_result[item_name] = int(item_amount) + pre_result[item_name]
            continue
        pre_result[item_name] = int(item_amount)

    result: list[str] = [
        name + " " + str(amount) for name, amount in pre_result.items()
    ]
    return sorted(sorted(result, key=sort_by_name), key=sort_by_amount, reverse=True)
