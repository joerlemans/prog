def calculate_grade(text: str) -> int:
    """
    Bepaalt aantal letters, woorden en zinnen van de tekst,
    en roept coleman_liau aan om grade te berekenen.
    
    >>> calculate_grade("One fish. Two fish. Red fish. Blue fish.")
    -9
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
    if text[-1] not in "!?.":
        sentences += 1
    return coleman_liau(words, sentences, letters)
    
    
def coleman_liau(words: int, sentences: int, letters: int) -> int:
    """
    Berekent de index volgens de Coleman Liau-formule.
    
    >>> coleman_liau(8, 4, 29)
    -9
    >>> coleman_liau(14, 4, 65)
    3
    """
    return round(0.0588 * (100 * letters / words) - 0.296 *
    (100 * sentences / words) - 15.8)

if __name__ == '__main__':
    result = input("Text: ")
    grade = calculate_grade(result)
    if grade < 1:
        print("Below Grade 1")
    if grade > 16:
        print("Grade 16+")
    else:
        print(f"Grade {grade}")