def ant(ans: str) -> bool:
    """
    Geeft True als ans gelijk is aan een van de correcte antwoorden en geeft anders False
    
    >>> is_correct("42")
    True
    >>> is_correct("Hallo")
    False
    >>> is_correct("100")
    False
    """
    if ans == "42" or ans == "tweeenveertig" or ans == "tweeënveertig":
        return True
    else:
        return False

if __name__ == '__main__':
    ans = str(input("Wat is het antwoord?"))
    result = ant(ans)
    if result == True:
        print("Ja")
    else:
        print("Nee")