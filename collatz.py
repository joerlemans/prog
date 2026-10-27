def print_collatz(n: int) -> int:
    """
    print de collatzreeks regel voor regel uit voor startwaarde n
    
    >>> print_collatz(3)
    3
    10
    5
    16
    8
    4
    2
    1
    >>> print_collatz(0)
    0
    """
    print(n)
    while n > 1:
        if n % 2 == 0:
            n = int(n / 2)
            print(n)
        else:
            n = n * 3 + 1
            print(n)

def collatz_length(n: int) -> int:
    """
    geeft de lengte van de collatzreeks voor startwwarde n
    
    >>> collatz_length(3)
    8
    >>> collatz_length(0)
    1
    """ 
    count = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            count += 1
        else:
            n = n * 3 + 1
            count += 1
    print(count)
