def is_priem(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_priem_tot(N: int) -> None:
    for i in range(2, N+1):
        


print(is_priem(1))