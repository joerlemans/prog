def is_same_rectangle(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    Controleert of de lengtes van de zijdes gelijk zijn
    
    >>> is_same_rectangle(6, 10, 10, 10)
    True
    >>> is_same_rectangle(6, 8, 7, 9)
    False
    >>> is_same_rectangle(0, 0, 0, 0)
    True
    """
    if ax_length == bx_length and ay_length == by_length:
        return True
    else:
        return False

def is_same_square(ax_length: int, ay_length: int, bx_length: int, by_length: int) -> bool:
    """
    Controleert of beide rechthoeken hetzelfde vierkant zijn
    
    >>> is_same_square(0, 0, 0, 0)
    True
    >>> is_same_square(6, 6, 6, 6)
    True
    >>> is_same_square(3, 4, 3, 3)
    False
    """
    if ax_length == ay_length == bx_length == by_length:
        return True
    else:
        return False

def calculate_length(c1: int, c2: int) -> int:
    """
    Berekent de lengte van een zijde op basis van twee coördinaten
    
    >>> calculate_length(3, 6)
    3
    >>> calculate_length(10, 4)
    6
    >>> calculate_length(0, 0)
    0
    """
    return abs(c2 - c1)

if __name__ == '__main__':
    
    ax1 = int(input("Geef de x1 van A: "))
    ax2 = int(input("Geef de x2 van A: "))
    ay1 = int(input("Geef de y1 van A: "))
    ay2 = int(input("Geef de y2 van A: "))
    bx1 = int(input("Geef de x1 van B: "))
    bx2 = int(input("Geef de x2 van B: "))
    by1 = int(input("Geef de y1 van B: "))
    by2 = int(input("Geef de y2 van B: "))
    
    ax_length = calculate_length(ax1, ax2)
    ay_length = calculate_length(ay1, ay2)
    bx_length = calculate_length(bx1, bx2)
    by_length = calculate_length(by1, by2)
    
    if is_same_rectangle(ax_length, ay_length, bx_length, by_length) == True:
        print("De rechthoeken zijn gelijk!")
    
    if is_same_square(ax_length, ay_length, bx_length, by_length) == True:
        print("En ze zijn ook nog vierkant!")
    
    else:
        print("Er is niks aan :(")
    
   