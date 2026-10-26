def is_schrikkel(year: int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    year = int(input("Welk jaar is het?"))
    result = is_schrikkel(year)
    if result == True:
        return 
    
    