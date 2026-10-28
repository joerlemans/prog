def convert_temperature(old_type: str, old_temp: int) -> int:
    """
    Zet de temperatuur (old_temp) van het type old_type om naar
    de temperatuur van het nieuwe type.
    """
    if old_type in {"c", "C"}:
        new_temp = (18 * old_temp + 320) / 10
        
    if old_type in {"f", "F"}:
        new_temp = (10 * old_temp - 320) / 18
    return new_temp

def print_table(old_type: str, begin_temp: int, end_temp: int, step_size: int) -> None:
    """
    Print de conversie-tabel.
    """
    if begin_temp == end_temp:
        print(" C |   F")
    
    
    while begin_temp < end_temp:
        print(f"{:3}")
        

if __name__ == '__main__':
    old_type = str(input("Welke eenheid van temperatuur (C of F)?"))
    while old_type not in {"c", "C", "f", "F"}:
        old_type = str(input("Welke eenheid van temperatuur (C of F)?"))
    begin_temp = int(input("Wat is de begintemperatuur?"))
    end_temp = int(input("Wat is de eindtemperatuur?"))
    step_size = int(input("Wat is de stapgrootte?"))
    while step_size < 1:
        step_size = int(input("Wat is de stapgrootte?"))
    print_table(old_type, begin_temp, end_temp, step_size)