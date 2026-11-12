def merge_lists(lst1: list[int], lst2: list[int]) -> list[int]:
    """
    """
    result = []
    i = 0
    j = 0
    while i or j < len(lst1) and len(lst2):
        if list1[i] > lst2[j]:
            result.append(lst2[j])
            j += 1
        else:
            result.append(lst1[i])
            i += 1
    if len(lst1) == len(lst2):
        return result
    if len(lst1) < len(lst2):
        length = len(lst2)
        start = j
    if len(lst1) > len(lst2):
        length = len(lst1)
        start = i
    for k in range(start,)