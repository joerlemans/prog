def contig(lst; list[object]) -> list[list[object]]:
    """
    >>> contig([1, 2, 3, 2, 3, 4])
    [[1, 2, 3], [2, 3, 4]]
    """
    contiguous = []
    new_lst = []
    for i in range(len(lst)):
        if lst[i] == contiguous[i] + 1:
            new_lst.append(i)
        else:
            contiguous.append(new_lst)
            
            
        