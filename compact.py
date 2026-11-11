def compact(lst: list[object]) -> list[object]:
    """
    """
    truthy = []
    for i in range(len(lst)):
        if i:
            truthy.append(lst[i])
    return truthy

print(compact([1, False, True, '', 0])
    