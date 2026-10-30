def is_priem(num: int) -> bool:
    """
    berekent of num een priemgetal is_priem
    >>> is_priem(7)
    True
    >>> is_priem(1)
    False
    >>> is_priem(7919)
    True
    """
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_priemen_tot(N: int) -> None:
    """
    print alle priemgetallen tot en met het getal N
    
    >>> print_priemen_tot(10)
    2
    3
    5
    7
    >>> print_priemen_tot(29)
    2
    3
    5
    7
    11
    13
    17
    19
    23
    29
    >>> print_priemen_tot(0)
    
    """
    for i in range(2, N+1):
        if is_priem(i) == True:
            print(i)
    return

def zoveelste_priem(N: int) -> int:
    """
    berekent het N'de priemgetal
    
    >>> zoveelste_priem(10)
    29
    >>> zoveelste_priem(1000)
    7919
    >>> zoveelste_priem(1)
    2
    """
    count = 0
    num = 2
    while count < N:
        if is_priem(num) == True:
            count += 1
            if count == N:
                return num
        num += 1
    return

if __name__ == '__main__':
    result = input("Naar het hoeveelste priemgetal bent u op zoek?")
    while result is not int:
        try:
            getal = int(result)
            if getal is abs
            break
        except ValueError:
            
    print(zoveelste_priem(result))
    

