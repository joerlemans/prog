def compact(lst: list[object]) -> list[object]:
    """
    >>> compact([1, False, True, '', 0])
    [1, True]
    >>> compact
    """
    truthy = []
    for i in range(len(lst)):
        if lst[i]:
            truthy.append(lst[i])
    return truthy

    