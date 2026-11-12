POINTS = [1, 3, 3,  2, 1, 4, 2, 4, 1, 8, 5, 1,  3,
          1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def compute_score(word: str) -> int:
    """
    Bereken en return de score voor het woord.
    
    >>> compute_score('code')
    7
    """
    score = 0
    for i in word:
        score += compute_letter_score(i)
    return score

def compute_letter_score(letter: str) -> int:
    """
    Bereken en return de score voor één enkele letter.
    
    """
    letter = letter.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    if letter not in alpha:
        return 0
    position = alpha.index(letter)
    return POINTS[position]

if __name__ == '__main__':
    result1 = input("Speler 1: ")
    result2 = input("Speler 2: ")
    score1 = compute_score(result1)
    score2 = compute_score(result2)
    if score1 == score2:
        print("Gelijkspel!")
    elif score1 > score2:
        print("Speler 1 wint!")
    else:
        print("Speler 2 wint!")