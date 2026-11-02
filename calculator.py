def evaluate(x: int, y: str, z: int) -> float:
    """
    Bereken het resultaat van de operatie y toegepast op x en z.
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

if __name__ == '__main__':
    x, y, z = input().split(" ")
    
    evaluate(x, y, z)
    