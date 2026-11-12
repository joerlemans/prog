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
        ind = l.index(value)
        l[sortd], l[ind] = l[i], l[sorted]