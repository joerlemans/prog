def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    
    >>> meal("7:15")
    'ontbijt'
    
    >>> meal("08:00")
    'ontbijt"
    
    >>> meal("13:00")
    "lunch"
    """
    hour, min = time.split(":")
    
    if hour in "07":
        return "ontbijt"
    if hour in "08" and min == "00":
        return "ontbijt"
    if hour == "12":
        return "lunch"
    if hour == "13" and min == "00":
        return "lunch"
    if hour == "18":
        return "avondeten"
    if hour == "19" and min == "00":
        return "avondeten"
    
    return None
 
    

if __name__ == '__main__':
    result = input("Hoe laat is het?")
    
    if meal(result) == "ontbijt":
        print("Het is tijd voor ontbijt")
    if meal(result) == "lunch":
        print("Het is tijd voor lunch")
    if meal(result) == "avondeten":
        print("Het is tijd voor avondeten")