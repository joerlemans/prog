from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> int:
    """
    vindt de langste reek niet-priemgetallen onder N
    
    >>> zoek_langste_reeks(10000)
    De langste reeks niet-priemgetallen onder de 10000 begint op
    9552 en eindigt bij {boven} De reeks is {boven - onder + 1} lang.
    """
    num = 2
    onder = 0
    langste_reeks = 0
    while num < N:
       
        if is_priem(num) == True:
            if is_priem(num - 1) == False:
                boven = num - 1
                if boven - onder > langste_reeks:
                    langste_reeks = boven - onder
                    langste_onder = onder
                    langste_boven = boven
            if is_priem(num + 1) == False:
                onder = num + 1
        num += 1
        
    return langste_onder, langste_boven

def print_boodschap(N: int, onder: int, boven: int) -> None:
    print(f"De langste reeks niet-priemgetallen onder de {N} begint op "
    f"{onder} en eindigt bij {boven} De reeks is {boven - onder + 1} lang.")
    return

if __name__ == '__main__':
    onder, boven = zoek_langste_reeks(10000)
    print_boodschap(10000, onder, boven)

