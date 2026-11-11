def compact(lst: list[object]) -> list[object]:
    """
    >>>compact(n1)
    [1, True]
    """
    truthy = []
    for i in range(len(lst)):
        if lst[i]:
            truthy.append(lst[i])
    return truthy

print(compact([1, False, True, '', 0]))
    