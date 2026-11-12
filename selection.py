def selection_sort(l: list[int]) -> list[int]:
    """
    Sorteert de lijst `l` door deze aan te passen.
    Er wordt geen nieuwe lijst gemaakt.
    Moet wel `l` returnen.
    """
    sortd = 0
    value = float('inf')
    for i in range(sortd, len(l)):
        if l[i] < value:
            value = l[i]
            l[sortd], l[i] = l[i], l[sorted]