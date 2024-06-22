def transformation(A: list[int], N: int) -> list[int]:
    """Return transformation transform of list."""
    B: list[int] = []
    for i in range(N):
        for j in range(N - i):
            k: int = i+j
            B.append(max(A[j:k+1]))
    return B

def TransformTransform(A: list[int], N: int) -> bool:
    """Return wheter is imperial hindrance."""
    first_transformation: list[int] = transformation(A, N)
    if sum(transformation(first_transformation, len(first_transformation))) % 2 == 0:
        return True
    return False




