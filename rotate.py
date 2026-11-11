def rotate(lst: list[object]) -> None:
    """
    >>> n1 = [1, 2, 3]
    >>> rotate(n1)
    >>> n1
    [2, 3, 1]
    """
    for i in len(lst):
        lst[i] = list[i + 1]