def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
    
    >>> evaluate("1", "+", "1")
    2.0
    
    >>> evaluate("100" - 9)
    91.0
    
    >>> evaluate(4 * -6)
    -24.0
    """
    x = float(x)
    z = float(z)
    
    if y == "+":
        return float(x + z)
    if y == "-":
        return float(x - z)
    if y == "*":
        return float(x * z)
    if y == "/":
        return float(x / z)
    
    return

if __name__ == '__main__':
    x, y, z = input().split(" ")
    print(evaluate(x, y, z))
    