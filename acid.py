def is_acidic(ph) -> bool:
    """
    Geeft True als de ph lager is dan 7.0 en False als deze hoger is.
    
    >>> is_acidic(6.0)
    True
    >>> is_acidic(9.0)
    False
    >>> is_acidic(0.0)
    True
    """
    if ph < 7.0:
        return True
    else:
        return False

if __name__ == '__main__':
    ph = float(input("Geef een pH-waarde: "))
    result = is_acidic(ph)
    if result == True:
        print("Het is een zuur")
    else:
        print("Het is een base")