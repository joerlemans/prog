def special_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    
    >>> special_sort([7, 4, 3, 9, 0, 2])
    [0, 2, 3, 4]
    """
    for i in range(len(l) - 1):
        for j in range(i, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    return l
