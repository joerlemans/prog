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
    if hour[1] == "2":
        return "lunch"
    if hour[1] == "3" and min == "00":
        return "ontbijt"
    if hour[1] == "8"
        
    
    
    
    if time[0].isdigit() == True and time[1].isdigit() == True:
        if time[1] in "23":
            return "lunch"
        if time[1] in "89":
            return "avondeten"
    
    

if __name__ == '__main__':
    <Vraag hier de gebruiker om invoer, roep je functie aan en print het antwoord>