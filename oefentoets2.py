def split_by_parity(ints: list[int])-> list[list[int]]:
    """
    >>> split_by_parity([1, 2, 3, 4])
    [[2, 4], [1, 3]]
    
    >>> 
    """
    even = []
    odd = []
    for i in ints:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]