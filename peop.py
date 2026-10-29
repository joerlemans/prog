def is_priem(num: int) -> bool:
    if num < 2:
        return False
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False  # Bij 9587 moet hij hier op vallen wanneer i = 13!
        i += 1
    return True

# Test direct
print("Test 9587:", is_priem(9587))  # Dit MOET False geven!