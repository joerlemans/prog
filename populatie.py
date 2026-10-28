def calculate_years(start_size: int, end_size: int) -> int:
    """
    Berekent het aantal jaar dat het duurt voor de populatie om
    end_size te bereiken.
    """
    count = 0
    while start_size < end_size:
        start_size = start_size + start_size / 3 - start_size / 4)
        count += 1
    return count
    

if __name__ == '__main__':
    start = int(input("Start populatie: "))
    while start < 9:
        start = int(input("Start populatie: "))
    end = int(input("Eind populatie: "))
    while end <= start:
        end = int(input("Eind populatie: "))
    print(calculate_years(start, end))
        
    