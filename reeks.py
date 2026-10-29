from priem_getal import is_priem

def zoek_langste_reeks(N: int) -> tuple:
    count = 2
    while count < N:
        if is_priem(count) == True:
            count += 1
            onder = count
            
        
    return onder, boven

def print_boodschap(N: int) -> None:
    
    return