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

def print_banner(lst: list[object]) -> str: