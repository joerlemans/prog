def check_input(dna: str) -> bool:
    """
    Controleert of de input een correcte DNA-string is.
    Accepteert zowel hoofd- als kleine letters.
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
    """
    rna = ""
    for i in dna.upper():
        if i ==  "A":
            rna = rna + "U"
        if i ==  "T":
            rna = rna + "A"
        if i ==  "C":
            rna = result + "G"
        if i ==  "G":
            result = result + "C"
    return rna

if __name__ == '__main__':
    result = input()
    while check_input(result) == False:
        result = input()
    print(transcribe_dna_to_rna(result))
    
        