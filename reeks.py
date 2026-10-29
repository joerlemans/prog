from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple:
    """
    geeft de langste reeks niet-priemgetallen onder N
    >>> zoek_langste_reeks(10000)
    

    """
    vorige_priem = 2
    onder = 0
    langste_onder = 0
    langste_boven = 0
    langste_reeks = 0
    for num in range(3, N):
        if is_priem(num) == True:
            onder = vorige_priem + 1
            boven = num - 1
            reeks = boven - onder
            if reeks > langste_reeks:
                langste_onder = onder
                langste_boven = boven
                langste_reeks = reeks
        vorige_priem = num
    return langste_onder, langste_boven

def print_boodschap(N: int, onder: int, boven: int) -> None:
    print(f"De langste reeks niet-priemgetallen onder de {N} begint op " 
    f"{onder} en eindigt bij {boven} De reeks is {boven - onder + 1} lang.")
    return

if __name__ == '__main__':
    onder, boven = zoek_langste_reeks(10000)
    print_boodschap(10000, onder, boven)

