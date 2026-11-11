def uniq(lst: list[object]) -> list[object]:
    """
    >>> uniq(['x', 'x', 1, 1, 0])
    ['x', 1, 0]
    
    >>> uniq([])
    """
    
    unique = []
    for i in lst:
        if i not in unique:
            unique.append(i)
    return unique
    