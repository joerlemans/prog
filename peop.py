def is_priem(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Check specifiek de getallen rondom het probleem
print("Is 9587 priem volgens de functie?:", is_priem(9587))
print("Is 9551 priem?:", is_priem(9551))
print("Is 9661 priem?:", is_priem(9661))