def sort_by_amount(item: str) -> int:
    """Return sold amount from item string."""
    return int(item.split()[1])


def sort_by_name(item: str) -> str:
    """Return item name from item string."""
    return item.split()[0]


def ShopOLAP(N: int, items: list[str]) -> list[str]:
    """Return grouped and sorted desc sold items and amount."""
    result: list[str] = []
    for i in items:
        if i.split()[0] not in [j.split()[0] for j in result]:
            result.append(i)
            continue
        for k, el in enumerate(result):
            if i.split()[0] == el.split()[0]:
                result[k] = (
                    el.split()[0] + " " + str(int(el.split()[1]) + int(i.split()[1]))
                )
                break

    return sorted(sorted(result, key=sort_by_name), key=sort_by_amount, reverse=True)
