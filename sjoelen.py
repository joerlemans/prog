import random
def calculate_points(board: list[int]) -> int:
    """
    Berekent het aantal punten dat is behaald met sjoelen. De
    volgorde van de punten is [2, 3, 4, 1]. Wanneer er een
    kwartet tussen zit, telt dit voor 20 punten.
    """

def shuffle_round(board: list[int], discs: int) -> int:
    """
    Simuleert een enkele ronde sjoelen. De variable `board` wordt
    aangepast als er een schijf in een gleuf terecht komt. Returnt
    het aantal schijven dat nog over is om nog eens mee te schuiven.
    """
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

if __name__ == '__main__':
    <Zet het bord klaar, simuleer drie rondes en
     bereken aan het eind het aantal punten op basis van
     de staat van het sjoelbord>
    start = [0, 0, 0, 0]