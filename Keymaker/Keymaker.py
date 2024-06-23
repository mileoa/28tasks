def Keymaker(k: int) -> str:
    """Return result of simulation of a key master`s work"""
    result: list[str] = ["0" for i in range(k)] # All doors are closed.

    for i in range(k):
        for j in range(i, k, i+1):
            if result[j] == "1":
                result[j] = "0"
                continue
            result[j] = "1"

    return "".join(result)




