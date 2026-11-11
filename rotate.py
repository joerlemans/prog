def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    """
    first = lst[0]
    print(len)
    for i in range(len(lst)):
        if i == len(lst):
            lst[i] = first
        lst[i] = lst[i + 1]