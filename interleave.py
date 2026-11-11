def interleave(lst1: list[object], lst2: list[object], keep: bool) -> list[object]:
    """
    interleave([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True)
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    """
    if len(lst2) > len(lst1):
        longest = lst2
        shortest = lst1
    else:
        longest = lst1
        shortest = lst2
    interlst = []
    for i in range(len(longest)):
        if i <= len(shortest):
            interlst.append(lst1[i])
            interlst.append(lst2[i])
        if i
        