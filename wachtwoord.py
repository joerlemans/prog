def check_length(password: str) -> bool:
    """
    Controleer of het wachtwoord minstens 8 karakters bevat.
    >>> check_length()
    """
    if len(password) > 8:
        return True
    return False

def check_letter(password: str) -> bool:
    """
    Controleer of het wachtwoord zowel een grote als een
    kleine letter bevat.
    Gebruik een loop om door password te lopen.
    """
    upp = False
    low = False
    for i in password:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            upp = True
        if i in "qwertyuiopasdfghjklzxcvbnm":
            low = True
        if upp == True and low == True:
            return True
    return False
        

def check_number(password: str) -> bool:
    """
    Controleer of het wachtwoord een cijfer bevat.
    Gebruik een loop om door password te lopen.
    """
    for i in password:
        if i in "0123456789":
            return True
    return False

def check_password(password: str) -> bool:
    """
    Controleer of aan alledrie de eisen is voldaan.
    """
    if check_length(password) == True and check_number(password) == True and check_letter(password) == True:
        return True
    else:
        return False

if __name__ == '__main__':
    result = input()
    if check_password(result) == True:
        print("Het gegeven wachtwoord is valide.")
    else:
        print("Het gegeven wachtwoord is niet valide.")