def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    
    >>> calculate_grade("Congratulations! Today is your day. You're "
    ...     "off to Great Places! You're off and away!")
    3
    >>> calculate_grade("There are more things in Heaven and Earth, "
    ...     "Horatio, than are dreamt of in your philosophy.")
    9
    """
    letters = 0
    words = 0
    sentences = 0
    for i in text:
        if i.isalpha():
            letters += 1
        if i == " ":
            words += 1
        if i == "." or i == "!" or i == "?":
            sentences += 1
    if text[-1] != " ":
        words += 1
    if text[-1] != ".":
        sentences += 1
    return coleman_liau(words, sentences, letters)
    
    
def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    """
    return round(0.0588 * (100 * letters / words) - 0.296 *
    (100 * sentences / words) - 15.8)

if __name__ == '__main__':
    result = input("Text: ")
    calculate_grade(result)