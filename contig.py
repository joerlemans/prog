def contig(lst; list[object]) -> list[list[object]]:
    """
    >>> contig([1, 2, 3, 2, 3, 4])
    [[1, 2, 3], [2, 3, 4]]
    """
    contiguous = []
    for i in range(len(lst)):
        if lst[i] == contiguous[i] + 1
        