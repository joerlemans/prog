def meal(time: str) -> str | None:
    """
    Converteert een tijd-string naar een maaltijd.
    De maaltijd kan zijn "ontbijt", "lunch", "avondeten".
    """
    hour, min = time.split(":")
    
    if hour in "07":
        return "ontbijt"
    if hour in "08" and min == "00":
        return "ontbijt"
    if hour == "2":
        return "lunch"
    if hour[1] == "3" and min == "00":
        return "ontbijt"
    if hour[1] == "8":
        return "avondeten"
    if hour[1] == "9" and min == "00":
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