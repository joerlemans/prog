def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    
    """
    letters = 0
    words = 0
    sentences = 0
    for i in text:
        if i.isalpha():
            letters += 1
        if i == " ":
            words += 1
        if i == ".":
            sentences += 1
    if text[-1] != " ":
        words += 1
    
    coleman_liau(words, sentences, letters)
    return
    
def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    """

if __name__ == '__main__':
    result = input()
    calculate_grade(result)