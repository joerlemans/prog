def build_pyramide(hoogte: int) -> int:
    """
    print een pyramide van haakjes
    
    >>> build_pyramide(5)
        ##
       
    """
    lvl = 1
    while lvl <= hoogte:
        for i in range(hoogte - lvl):
            print(' ', end='')
        for i in range(lvl + 1):
            print('#', end='')
        lvl += 1
        print()
    return lvl
        
if __name__ == '__main__':
    hoogte = int(input("Hoe hoog is de pyramide? (max 23)"))
    while hoogte > 23:
        hoogte = int(input("Hoe hoog is de pyramide? (max 23)"))
    build_pyramide(hoogte)