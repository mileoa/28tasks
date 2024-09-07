def SynchronizingTables(N: int, ids: list[int], salary: list[int]) -> list[int]:

    ids_copy: list[int] = ids.copy()

    ids_copy.sort()
    salary.sort()

    ids_salary: dict[int, int] = {}
    for i in range(N):
        ids_salary[ids_copy[i]] = salary[i]

    for i in range(N):
        salary[i] = ids_salary[ids[i]]

    return salary
