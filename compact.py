def compact(lst: list[object]) -> list[object]:
    """
    >>> n1 = [1, False, True, '', 0]
    >>> compact(n1)
    >>> n1
    []
    """
    truthy = []
    for i in range(len(lst)):
        if lst[i]:
            truthy.append(lst[i])
    return truthy

print(compact([1, False, True, '', 0]))
    