def select_not_lower(strs: list[str])-> list[str]:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['Roep', 'Hallo']
    """
    upper = []
    for i in range(len(strs)):
        