def chunk(n: int, lst: list[object]) -> list[list[object]]:
    """
    >>> chunk(3, [1, 2, 4, 3, 1, 1, 4, 5, 6])
    [[1, 2, 4], [3, 1, 1], [4, 5, 6]]
    
    >>> chunk(2, [1, 4, 3, 5, 6])
    [[1, 4], [3, 5], [6]]
    
    >>> chunk(10, [1, 2, 3, 5])
    [[1, 2, 3, 5]]
    """
    chunk_1 = []
    new_1 = []
    for i in lst:
        if len(new_1) >= n:
            chunk_1.append(new_1)
            new_1 = []
        new_1.append(i)
    chunk_1.append(new_list)
    return chunk_list    