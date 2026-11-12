def longest_word_from_list(lst: list[object]) -> str:
    """
    >>> 
    """
    longest = ''
    for i in lst:
        if len(i) > len(longest):
            longest = i
    return longest