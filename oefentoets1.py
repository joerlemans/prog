def select_not_lower(strs: list[str])-> list[str]:
    """
    >>> select_not_lower(['Roep', 'maar', 'HALLO'])
    ['Roep', 'HALLO']
    
    >>> select_not_lower(['YO'])
    ['YO']
    
    >>> select_not_lower(['hoi', 'hallo', 'doei'])
    []
    
    >>> select_not_lower([])
    []
    """
    upper = []
    for i in strs:
        if i.islower() == False:
            upper.append(i)
    return upper

def string_picker(strs: list[str], picks: list[int])-> str:
    """
    >>> string_picker(['a', 'dd'], [0, 0, 1])
    'aadd'
    """
    output = ''
    for i in
    