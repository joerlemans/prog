def contig(lst: list[int]) -> list[list[int]]:
    """
    >>> contig([1, 2, 3, 2, 3, 4])
    [[1, 2, 3], [2, 3, 4]]
    
    >>> contig([3, 4, 1, 6, 7, 8, 1, 3])
    [[3, 4], [1], [6, 7, 8], [1], [3]]
    
    >>> contig([1, 1, 1])
    [[1], [1], [1]]
    """
    if lst
    contiguous = []
    new_lst = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] == new_lst[len(new_lst) - 1] + 1:
            new_lst.append(lst[i])
        else:
            contiguous.append(new_lst)
            new_lst = [lst[i]]
    contiguous.append(new_lst)
    return contiguous