def remove_vowels(text: srt) -> str:
    """
    haalt de klinkers uit text
    
    >>> remove_vowels("")
    """
    result = ""
    for i in text:
        if i not in "euioa":
            result = result + i
    return result