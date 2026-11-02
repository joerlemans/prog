def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    
    >>> evaluate(1 + 1)
    2.0
    
    >>> evaluate(100 - 9)
    91.0
    
    >>> evaluate()
    """
    x = int(x)
    z = int(z)
    
    if y == "+":
        return float(x + z)
    if y == "-":
        return float(x - z)
    if y == "*":
        return float(x * z)
    if y == "/":
        return float(x / z)

if __name__ == '__main__':
    x, y, z = input().split(" ")
    print(evaluate(x, y, z))
    