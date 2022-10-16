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
    sum = 0
    for index, row in enumerate(matrix):
        sum = sum+row[index]+row[-1-index]
    return sum


m1 = [
    [1,   2],
    [30, 40],
]
print(sum_up_diagonals(m1))

m2 = [

    [1, 2, 3],

    [4, 5, 6],

    [7, 8, 9],
]
print(sum_up_diagonals(m2))
