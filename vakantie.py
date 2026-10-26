def travel_costs(km: int) -> float:
    """
    Bepaalt de vervoerskosten op basis van de te rijden afstand
    naar de accomodatie (tel `km` twee keer voor heen en terug).
    
    >>> travel_costs(10)
    2.6
    >>> travel_costs(3)
    0.78
    >>> travel_costs(0)
    0
    """
    return km * 0.26

def overnight_costs(nights: int) -> float:
    """
    Bepaalt de overnachtingskosten op basis van het aantal nachten
    dat je op vakantie gaat.
    
    >>> overnight_costs(100)
    6000
    >>> overnight_costs(5)
    300
    >>> overnight_costs(0)
    0
    """
    return nights * 60

def total_costs(km: int, nights: int) -> int:
    """
    Bepaalt de totale kosten op basis van de afstand en het aantal
    nachten en rondt af naar hele euro's.
    Deze functie delegeert zoveel mogelijk werk naar de andere
    twee functies (roep die dus hier aan).
    
    >>> total_costs()
    """
    return km * 0.26 + nights * 60

if __name__ == '__main__':
    <Schrijf hier code die input van de gebruiker opvraagt,
    total_costs aanroept, en print hoeveel de vakantie gaat kosten>