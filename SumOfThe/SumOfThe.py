def SumOfThe(N: int, data: list[int]) -> int:
    for i, num in enumerate(data):
        sum_of: int = 0
        for j in data[:i] + data[i + 1 :]:
            sum_of += j
        if sum_of == num:
            return num
