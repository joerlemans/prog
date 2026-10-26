def check_answer(answer: str) -> bool:
    """
    Controleer of het antwoord op de vraag één van de opties
    42, tweeenveertig, of tweeënveertig is.
    
    >>> check_answer("42")
    True
    >>> check_answer("Hallo")
    False
    >>> is_correct("100")
    False
    """
    if answer == "42" or answer == "tweeenveertig" or answer == "tweeënveertig":
        return True
    else:
        return False

if __name__ == '__main__':
    answer = str(input("Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?"))
    result = check_answer(answer)
    if result == True:
        print("Ja")
    else:
        print("Nee")