def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    sortd = 0
    while sortd < len(l):
        value = float('inf')
        for i in range(sortd, len(l)):
            if l[i] < value:
                value = l[i]
                ind = i
        l[sortd], l[ind] = l[ind], l[sortd]
        sortd += 1
    return l
    
print(selection_sort([4, 3, 2, 1]))