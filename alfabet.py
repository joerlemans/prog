def compare(word1: str, word2: str) -> int:
    """
    Kijkt welk woord eerder in het alfabet voorkomt.
    Geeft -1 terug als word1 eerst komt, 1 als word2 eerst komt, 
    en 0 als de woorden exact gelijk zijn.
    
    >>> compare("Jan", "bert")
    1
    >>> compare("zekrom", "zygarde")
    -1
    >>> compare("Henk", "Henk")
    0
    """
    w1 = word1.lower()
    w2 = word2.lower()
    
    if w1 < w2:
        return -1
    elif w1 > w2:
        return 1
    else:
        return 0


if __name__ == '__main__':
    word1 = input("Woord 1: ")
    word2 = input("Woord 2: ")
    
    result = compare(word1, word2)
    if result == -1:
        print(f"{word1} first")
    elif result == 1:
        print(f"{word2} first")
    else:
        print("No need to decide!")