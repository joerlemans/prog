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
    
    >>> string_picker(['a', 'b', 'c'], [0, 1, 2])
    'abc'
    
    >>> string_picker([],[])
    ''
    
    >>> string_picker(['a'], [])
    ''
    """
    output = ''
    for i in picks:
        output += strs[i]
    return output

def remove_prefix(s: str, prefix: str)-> str:
    """
    >>> remove_prefix('toedeloe', 'toe')
    'deloe'
    """
    output = ''
    while:
        
def most_vowely_word(sentence: str)-> str:
    """
    >>> most_vowely_word('de groene kamer')
    'groene'
    """
    output = ''
    most = 0
    vowels = 0
    word = ''
    for i in sentence:
        if i.lower() is in 'aeiou':
            vowels + 1
        elif i == ' ':
            if vowels >= most:
                most = vowels
                output
        else:
            word += i
            

