def chunk(lst: list[object], n: int) -> list[list[object]]:
    """
    >>> chunk([1, 2, 4, 3, 1, 1, 4, 5, 6], 3)
    [[1, 2, 4], [3, 1, 1], [4, 5, 6]]
    
    >>> chunk([1, 4, 3, 5, 6], 2)
    [[1, 4], [3, 5], [6]]
    
    >>> chunk([1, 2, 3, 5], 10)
    [[1, 2, 3, 5]]
    
    >>> chunk([], 4)
    []
    """
        
    chunk_1 = []
    if len(lst) != 0:
        new_1 : list[object] = []
        for i in lst:
            if len(new_1) >= n:
                chunk_1.append(new_1)
                new_1 = []
            new_1.append(i)
    chunk_1.append(new_1)
    return chunk_1    