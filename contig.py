def contig(lst: list[object]) -> list[list[object]]:
    """
    >>> contig([1, 2, 3, 2, 3, 4])
    [[1, 2, 3], [2, 3, 4]]
    """
    contiguous = []
    new_lst = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == new_lst[len(new_lst) -:
            new_lst.append(lst[i])
        else:
            contiguous.append(new_lst)
            new_lst = []
    return contiguous
        