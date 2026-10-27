def count_coins(cents: int) -> int:
    """
    Berekent het minimale aantal munten (25, 10, 5 en 1 cent)
    waarmee het bedrag `cents` kan worden teruggegeven.
    """

if __name__ == '__main__':
    result = float(input("Voer een bedrag in: "))
    while result <= 0.0:
        result = float(input("Voer een bedrag in: "))
    resul = result * 100
    print(count_coins(result)
    
    <Vraag om het bedrag tot het geldig is, zet het om naar centen,
    roep de functie aan en print het aantal munten>