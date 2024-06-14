def TankRush(H1: int, W1:int, S1: str, H2:int, W2: int, S2: str) -> bool:
    """Decide if first map contains second map."""
    matrix_s1: list[list[str]] = [list(i) for i in S1.split()]
    matrix_s2: list[list[str]] = [list(i) for i in S2.split()]

    next_j: bool = False
    for i in range(H1): # Lines.
        for j in range(W1): # Columns.

            next_j = False
            if matrix_s1[i][j] != matrix_s2[0][0]:
                continue

            # If found begin of second matrix then compare.
            for k in range(H2): # Lines.

                # Check out of range.
                if k + i > H1-1:
                    next_j = True
                    break

                for l in range(W2):  # Columns.

                    # Check out of range.
                    if j + l > W1-1:
                        next_j = True
                        break

                    # Use second matrix indexes as offset.
                    if matrix_s2[k][l] != matrix_s1[i+k][j+l]:
                        next_j = True
                        break

                if next_j:
                    break
            if next_j:
                continue

            # Comparing of second matrix completed without break.
            return True

    return False




