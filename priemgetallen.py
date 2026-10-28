def is_priem(num: int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def print_priem_
print(is_priem())