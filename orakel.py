def check_answer(answer: str) -> bool:
    """
    Controleer of het antwoord op de vraag één van de opties
    42, tweeenveertig, of tweeënveertig is.
    
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
    answer = str(input("Wat is het antwoord?"))
    result = (ancs)
    if result == True:
        print("Ja")
    else:
        print("Nee")