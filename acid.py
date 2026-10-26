def is_acidic(ph) -> bool:
    if ph < 7.0:
        return True
    else:
        return False

if __name__ == '__main__':
    ph = float(input("Geef een pH-waarde: "))
    result = is_acidic(ph)