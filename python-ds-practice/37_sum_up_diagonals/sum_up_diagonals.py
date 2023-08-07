def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    TL_Diag = 0
    TR_Diag = 0

    i = 0
    j = 0
    while i < len(matrix):
        TL_Diag += matrix[i][i]
        i += 1

    while i > 0:
        TR_Diag += matrix[j][i-1]
        i -= 1
        j += 1
    return TL_Diag + TR_Diag

    