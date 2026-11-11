def uniq(lst: list[object]) -> list[object]:
    """
    >>> uniq(['x', 'x', 1, 1, 0])
    ['x', 1, 0]
    
    >>> uniq([1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique
    