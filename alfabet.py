def compare(word1: str, word2: str) -> int:
    """
    kijkt welke letter eerder in het alfabet voorkomt
    
    >>> compare("Jan", "bert")
    1
    >>> compare("zekrom", "zygarde")
    0
    >>> compare("Henk", "Klaas")
    -1
    """
    
    L1 = word1[0].upper()
    L2 = word2[0].upper()
    
    if L1 == L2:
        return 0
    if L1 < L2:
        return -1
    if L1 > L2:
        return 1
    
    

if __name__ == '__main__':
    
    