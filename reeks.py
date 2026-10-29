from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple:
    num = 0
    onder = 0
    while num < N:
       
        if is_priem(num) == True and is_priem(num - 1) == False:
            boven = num - 1
            reeks = boven - onder
            if reeks > langste_reeks
        if is_priem(num) == True and is_priem(num + 1) == False:
            onder = num + 1
       
       
        num += 1 
        
    return onder, boven

def print_boodschap(N: int) -> None:
    
    return