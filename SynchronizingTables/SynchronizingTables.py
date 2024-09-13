def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:
    """
    Return salary list, which ordered to be valid for employee on the same index in ids list.
    Ordered asc ids equel ordered asc salary.
    """
    ids_copy: list[int] = ids.copy()
    salary_copy: list[int] = salary.copy()
    ids_copy.sort()
    salary_copy.sort()

    ids_salary: dict[int, int] = {}
    for i in range(N):
        ids_salary[ids_copy[i]] = salary_copy[i]

    for i in range(N):
        salary_copy[i] = ids_salary[ids[i]]

    return salary_copy
