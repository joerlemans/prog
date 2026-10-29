from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple:
    num = 0
    onder = 0
    boven = None
    langste_reeks = 0
    langste_onder = None
    langste_boven = None
    while num < N:
       
        if is_priem(num) == True and is_priem(num - 1) == False:
            boven = num - 1
            reeks = boven - onder + 1
        if reeks > langste_reeks:
            langste_reeks = reeks
            langste_onder = onder
                langste_boven = boven
        if is_priem(num) == True and is_priem(num + 1) == False:
            onder = num + 1
        num += 1 
        
    return langste_onder, langste_boven

def print_boodschap(N: int) -> None:
    
    return

print(zoek_langste_reeks(10))