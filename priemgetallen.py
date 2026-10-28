def is_priem(num: int) -> bool:
    """
    berekent of num een priemgetal is_priem
    >>>is_priem(7)
    True
    >>>is_priem(1)
    False
    >>>is_priem()
    """
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
    N = input("Naar het hoeveelste priemgetal bent u op zoek?")
    while N is not abs and int:
        N = input("Naar het hoeveelste priemgetal bent u op zoek?")
    print(zoveelste_priem(N))

