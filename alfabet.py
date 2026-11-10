def compare(word1: str, word2: str) -> int:
    """
    kijkt welke letter eerder in het alfabet voorkomt
    
    >>> compare("Jan", "bert")
    1
    >>> compare("zekrom", "zygarde")
    -1
    >>> compare("Henk", "Henk")
    -1
    """
    if wor
    
    for i in word1:
        for j in word2:
            if i.upper
    
    while True:
        c = 0
        L1 = word1[c].upper()
        L2 = word2[c].upper()
        if L1 == L2:
            c += 1
        if L1 < L2:
            return -1
        if L1 > L2:
            break
    
    
if __name__ == '__main__':
    word1 = input("Woord 1: ")
    word2 = input("Woord 2: ")
    if compare(word1, word2) == -1:
        print(f"{word1} first")
    if compare(word1, word2) == 1:
        print(f"{word2} first")
    if compare(word1, word2) == 0:
        print("No need to decide!")
    
    