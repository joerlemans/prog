def interleave(lst1: list[object], lst2: list[object], keep: bool) -> list[object]:
    """
    interleave([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], True)
    [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    """
    if len(lst2) > len(lst1):
        twee = True
    else:
        twee = False
    
    interlst = []
    for i in range(len(lst2)):
        if lst2[i] not in interlst:
            
        