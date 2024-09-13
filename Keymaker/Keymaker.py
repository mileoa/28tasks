CLOSED_DOOR_SIGN = "0"
OPENED_DOOR_SIGN = "1"


def Keymaker(k: int) -> str:
    """Return result of simulation of a key master`s work"""
    doors_status_after_simulation: list[str] = [
        CLOSED_DOOR_SIGN for i in range(k)
    ]  # All doors are closed.

    # Change status of door.
    # k == 1 then change all doors.
    # k == 2 then change every second door.
    # k == 3 then change evety third second door and so on
    for i in range(k):
        for j in range(i, k, i + 1):
            if doors_status_after_simulation[j] == OPENED_DOOR_SIGN:
                doors_status_after_simulation[j] = CLOSED_DOOR_SIGN
                continue
            doors_status_after_simulation[j] = OPENED_DOOR_SIGN

    return "".join(doors_status_after_simulation)
