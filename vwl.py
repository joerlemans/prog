def remove_vowels(text: srt) -> str:
    """
    haalt de klinkers uit text
    
    >>> remove_vowels("just setting up my twitter")
    """
    result = ""
    for i in text:
        if i not in "euioa":
            result = result + i
    return result