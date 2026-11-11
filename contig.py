def contig(lst: list[object]) -> list[list[object]]:
    """
    >>> contig([1, 2, 3, 2, 3, 4])
    [[1, 2, 3], [2, 3, 4]]
    """
    contiguous = []
    new_lst = []
    for i in range(len(lst)):
        
        if lst[i] == new_lst[i] + 1:
            new_lst[i]
        else:
            contiguous.append(new_lst)
            new_lst = []
    return contiguous
        