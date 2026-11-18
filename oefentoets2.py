def split_by_parity(ints: list[int])-> list[list[int]]:
    """
    >>> split_by_parity([1, 2, 3, 4])
    [[2, 4], [1, 3]]
    
    >>> split_by_parity([])
    [[], []]
    
    >>> split_by_parity([2, 2, 4, 4])
    [[2, 2, 4, 4], []]
    
    >>> split_by_parity([1, 3])
    [[], [1, 3]]
    """
    even = []
    odd = []
    for i in ints:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return [even, odd]

def reading_level(s: str)-> float:
    """
    >>> reading_level('Mijn naam is Pim')
    9.75
    
    >>> reading_level('')
    0.0
    
    >>> reading_level('hoi')
    -3.0
    """
    klink = 0
    mede = 0
    words = 0
    for i in s:
        if i.lower() in 'aeiou':
            klink += 1
        elif i == ' ':
            words +=1
        else:
            mede += 1
    words += 1
    length = (klink + mede) / words
    return round(((mede - klink) * length), 2)

def longest_word_length(s: str)-> int:
    """
    >>> longest_word_length('lahetetty joensuun hotellista')
    10
    
    >>> longest_word_length('e en jij bent eerst cool')
    5
    
    >>> longest_word_length('dit is een test bondgenootschap idee')
    15
    """
    longest = 0
    current = 0
    for i in s:
        if i == ' ' and current > longest:
            longest = current
            current = 0
        elif i == ' ':
            current = 0
        else:
            current += 1
    if current > longest:
        longest = current
    return longest

def encrypt(s: str)-> str:
    """
    >>> encrypt('abc')
    'zyx'
    """
    alfa = 'abcdefghijklmnopqrtsuvwxyz'
    encr = ''
    for i in s:
        pos = 0
        for k in alfa:
            if i == k:
                break
            pos += 1
        posr = 25 - pos
        pos= 0
        for l in alfa:
            if pos == posr:
                encr += l
            


    