def select_not_lower(strs: list[str])-> list[str]:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['Roep', 'HALLO']
    
    >>> select_not_lower([])
    """
    upper = []
    for i in strs:
        for j in i:
            if j.isupper():
                upper.append(i)
                break
    return upper