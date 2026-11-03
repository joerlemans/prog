def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA-string is.
    Accepteert zowel hoofd- als kleine letters.
    
    >>> check_input("bla bla")
    False
    
    >>> check_input("actg")
    True
    """
    for i in dna.upper():
        if i not in "AGCT":
            return False
    return True

def transcribe_dna_to_rna(dna: str) -> str:
    """
    Schrijft een string met DNA-elementen in hoofd- en/of kleine
    letters om naar een string met RNA-elementen (als hoofdletters).
    Ga ervan uit dat een valide string wordt gegeven (dus geen
    check aanroepen).
    
    >>> transcribe_dna_to_rna("ACgt")
    'UGCA'
    
    >>> transcribe_dna_to_rna("AAAGGGTTTCCC")
    'UUUCCCAAAGGG'
    """
    rna = ""
    for i in dna.upper():
        if i ==  "A":
            rna = rna + "U"
        if i ==  "T":
            rna = rna + "A"
        if i ==  "C":
            rna = rna + "G"
        if i ==  "G":
            rna = rna + "C"
    return rna

if __name__ == '__main__':
    result = input("DNA: ")
    while check_input(result) == False:
        result = input("DNA: ")
    print(f"RNA: {transcribe_dna_to_rna(result)}")
    
        