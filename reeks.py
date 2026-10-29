from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple:
    num = 2
    onder = 3
    boven = 4
    while num < N:
        if is_priem(num) == True and num < boven:
            onder = num
        if is_priem(num) == True and num > onder:
            
        num += 1 
        
    return onder, boven

def print_boodschap(N: int) -> None:
    
    return