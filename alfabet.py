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
    return
if __name__ == '__main__':
    word1 = input("Woord 1: ")
    word2 = input("Woord 2: ")
    if compare(word1, word2) == -1:
        print(f"{word1} first")
    if compare(word1, word2) == 1:
        print(f"{word2} first")
    if compare(word1, word2) == 0:
        print("No need to decide!")
    
    