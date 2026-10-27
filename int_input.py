def get_positive_int() -> int:
    """
    checkt of de input een positieve integer is 
    """
    result = int(input("Voer een positieve integer in: "))
    while result < 1:
        result = int(input("Voer een positieve integer in: "))
    return result

def get_any_int_but_0() -> int:
    """
    checkt of de input een integer behalve 0 is
    """
    result = int(input("Voer een integer in behalve 0: "))
    while result == 0:
        result = int(input("Voer een integer in behalve 0: "))
    return result

def get_min_int(n) -> int:
    """
    """
    result = int(input("Voer een integer in van minimaal 100: "))
    while result < n:
        result = int(input("Voer een integer in van minimaal 100: "))
    return

if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()