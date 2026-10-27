def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.
    >>> count_coins(662)
    29
    >>> c
    """
    count = 0
    while cents >= 25:
        cents -= 25
        count += 1
    while cents >= 10:
        cents -= 10
        count += 1
    while cents >= 5:
        cents -= 5
        count += 1
    while cents >= 1:
        cents -= 1
        count += 1
    return count 

if __name__ == '__main__':
    result = float(input("Voer een bedrag in: "))
    while result <= 0.0:
        result = float(input("Voer een bedrag in: "))
    result = round(result * 100)
    print(count_coins(result))
    
