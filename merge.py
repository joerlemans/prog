def merge_lists(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    >>> merge_lists([1, 2, 5], [4, 5, 6])
    [1, 2, 4, 5, 5, 6]
    """
    result = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] > lst2[j]:
            result.append(lst2[j])
            j += 1
        else:
            result.append(lst1[i])
            i += 1
    if i < j:
        length = len(lst2)
        lst3 = lst2
        start = j
    if i > j:
        length = len(lst1)
        lst3 = lst1
        start = i
    else:
        return result
    for k in range(start, length):
        result.append(lst3[k])
    return result