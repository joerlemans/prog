def is_priem(num: int) -> bool:
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_priem_tot(N: int) -> None:
    for i in range(2, N+1):
        if is_priem(i) == True:
            print(i)
    return

def zoveelste_priem(N: int) -> int:
    count = 0
    num = 2
    while count < N:
        if is_priem(num) == True:
            count += 1
            if count == N:
                return num
        num += 1

if __name__ == '__main__':
    N = int(input("Naar het hoeveelste priemgetal bent u op zoek?"))
    

