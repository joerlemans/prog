from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple:
    num = 2
    onder = 4
    boven = 4
    while num < N:
        while num > onder:
            if is_priem(num) == True:
                
        
        
        if is_priem(num) == True and num <= boven:
            
            onder = num + 1
        if is_priem(num) == True and num >= onder:
            boven = num - 1
        if
        num += 1 
        
    return onder, boven

def print_boodschap(N: int) -> None:
    
    return