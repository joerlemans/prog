def chunk(n: int, lst: list[object]) -> list[list[object]:
    """
    >>> chunk(3, [1, 2, 4, 3, 1, 1, 4, 5, 6])
    [[1, 2, 4], [3, 1, 1], [4, 5, 6]]
    
    >>> chunk(2, [1, 4, 3, 5, 6])
    [[1, 4], [3, 5], [6]]
    
    >>> chunk(10, [1, 2, 3, 5])
    [[1, 2, 3, 5]]
    """
    chunk_list = []
    new_list = []
    for i in lst:
        if len(new_list) >= n:
            chunk_list.append(new_list)
            new_list = []
        new_list.append(i)
    chunk_list.append(new_list)
    return chunk_list    