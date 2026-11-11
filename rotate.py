def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    """
    first = lst[0]
    for i in range(len(lst)):
        if i == len(lst) - 1:
            lst[i] = first
        else:
            lst[i] = lst[i + 1]
    return lst
    
    
rotate([1, 2, 3])