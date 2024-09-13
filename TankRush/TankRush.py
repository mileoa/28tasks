def TankRush(H1: int, W1: int, S1: str, H2: int, W2: int, S2: str) -> bool:
    """Decide if first map contains second map."""
    matrix_s1: list[list[str]] = [list(i) for i in S1.split()]
    matrix_s2: list[list[str]] = [list(i) for i in S2.split()]

    will_be_processed_next_column: bool = False
    for map_line_number in range(H1):
        for map_column_number in range(W1):

            will_be_processed_next_column = False
            if matrix_s1[map_line_number][map_column_number] != matrix_s2[0][0]:
                continue

            # If found begin of second matrix then compare.
            for k in range(H2):  # Lines.

                # Check out of range.
                if k + map_line_number > H1 - 1:
                    will_be_processed_next_column = True
                    break

                for l in range(W2):  # Columns.

                    # Check out of range.
                    if map_column_number + l > W1 - 1:
                        will_be_processed_next_column = True
                        break

                    # Use second matrix indexes as offset.
                    if (
                        matrix_s2[k][l]
                        != matrix_s1[map_line_number + k][map_column_number + l]
                    ):
                        will_be_processed_next_column = True
                        break

                if will_be_processed_next_column:
                    break
            if will_be_processed_next_column:
                continue

            # Comparing of second matrix completed without break.
            return True

    return False
