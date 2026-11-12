def longest_word_from_list(lst: list[object]) -> str:
    """
    >>> longest_word_from_list(['hoi', 'hallo', 'haai'])
    'hallo'
    """
    longest = ''
    for i in lst:
        if len(i) > len(longest):
            longest = i
    return longest

def print_banner(lst: list[object]) -> None:
    """
    >>> print_banner(['hoi', 'hallo', 'haai'])
    #####
    hoi
    hallo
    haai
    #####
    """
    size = len(longest_word_from_list(lst))
    for i in range(size):
        print('#', end='')
    print()
    for i in lst:
        print(i)
    for i in range(size):
        print('#', end='')
    return

def string_to_list(sent: str) -> list[object]:
    """
    >>> string_to_list('Hoi dit is een zin')
    ['Hoi', 'dit', 'is', 'een', 'zin']
    
    >>> string_to_list('soms, is een zin, wat lastiger)
    """
    word_lst = []
    new_word = ''
    for i in sent:
        if i.isalpha():
            new_word += i
        elif len(new_word) > 0:
            word_lst.append(new_word)
            new_word = ''
    word_lst.append(new_word)
    return word_lst

    