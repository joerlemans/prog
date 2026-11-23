import random
def calculate_points(board: list[int]) -> int:
    """
    Berekent het aantal punten dat is behaald met sjoelen. De
    volgorde van de punten is [2, 3, 4, 1]. Wanneer er een
    kwartet tussen zit, telt dit voor 20 punten.
    
    >>> calculate_points([4, 3, 3, 5])
    64
    
    >>> calculate_points([2, 4, 6, 2])
    62
    
    >>> calculate_points([6, 2, 3, 7])
    57
    """
    points = [2, 3, 4, 1]
    result = 0
    lowest = 100
    for j in board:
        if j < lowest:
            lowest = j
    result += 20 * lowest
    for p in range(4):
        board[p] -= lowest
    for q in range(4):
        result += board[q] * points[q]
    return result

def shuffle_round(board: list[int], discs: int) -> int:
    """
    Simuleert een enkele ronde sjoelen. De variable `board` wordt
    aangepast als er een schijf in een gleuf terecht komt. Returnt
    het aantal schijven dat nog over is om nog eens mee te schuiven.
    """
    scored = 0
    for i in range(discs):
        x = random.uniform(0, 1)
        if x <= 0.25:
            y = random.uniform(0, 1)
            if y <= 0.3:
                board[0] += 1
            elif 0.3 < y <= 0.5:
                board[1] += 1
            elif 0.5 < y <= 0.7:
                board[2] += 1
            else:
                board[3] += 1
            scored += 1
    return discs - scored

if __name__ == '__main__':
    board = [0, 0, 0, 0]
    discs = 30
    for k in range (3):
        discs = shuffle_round(board, discs)
    print(f"Je bent geëindigd op deze configuratie: {board}")
    print(f"Dat zijn {calculate_points(board)} punten!")