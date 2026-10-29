from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple:
    num = 0
    onder = 0
    boven = 1
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

def print_boodschap(N: int) -> None:
    
    return

print(zoek_langste_reeks(10))