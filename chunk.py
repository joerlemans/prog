def chunk(n: int, lst: list[object]) -> list[object]:
    """
    >>> chunk(3, [])
    """
    chunk_list = []
    new_list = []
    for i in lst:
        if len(new_list) >= n:
            chunk_list.append(new_list)
            new_list = []
        new_list.append(i)
    return chunk_list    