def get_positive_int() -> int:
    """
    """
    result = int(input("Voer een positieve integer in: "))
    while result < 1:
        result = int(input("Voer een positieve integer in: "))
    return result

def get_any_int_but_0() -> int:
    """
    """
    
    





if __name__ == '__main__':
    get_positive_int()
    get_any_int_but_0()
    get_min_int(100)
    get_two_different_ints()