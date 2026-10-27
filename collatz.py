def print_collatz(n):
    """
    print de collatzreeks regel voor regel uit voor startwaarde n
    
    >>> print_collatz(3)
    3
    10
    5.0
    16.0
    8.0
    4.0
    2.0
    1.0
    >>> print_collatz(0)
    0
    """
    print(n)
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            print(n)
        else:
            n = n * 3 + 1
            print(n)

def collatz_length(n):
    """
    geeft de lengte van de collatzreeks uit voor 
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

print_collatz(3)
collatz_length(3)