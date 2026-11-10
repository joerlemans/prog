def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    
    >>> evaluate(1, "+", 1)
    2.0
    
    >>> evaluate(100, "-", 9)
    91.0
    
    >>> evaluate(4, "*", -6)
    -24.0
    """
    
    if y == "+":
        return float(x + z)
    if y == "-":
        return float(x - z)
    if y == "*":
        return float(x * z)
    if y == "/":
        return float(x / z)
    
    return 0.0

if __name__ == '__main__':
    x1, y, z1 = input().split(" ")
    x = int(x1)
    z = int(z1)
    print(evaluate(x, y, z))
    