def remove_vowels(text: srt) -> str:
    """
    haalt de klinkers uit text
    
    >>> remove_vowels("just setting up my twitter")
    'jst sttng p my twttr'
    
    >>> remove_vowels("hello")
    'hll'
    """
    result = ""
    for i in text:
        if i not in "euioa":
            result = result + i
    return result

if __name__ == '__main__':
    inp = input()
    print(remove_vowels(inp))