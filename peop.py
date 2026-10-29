def is_priem(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

vorig_priem = 2
langste_reeks = 0
langste_onder = 0
langste_boven = 0

for num in range(3, 10000):
    if is_priem(num):
        onder = vorig_priem + 1
        boven = num - 1
        lengte = boven - onder + 1

        if lengte > langste_reeks:
            langste_reeks = lengte
            langste_onder = onder
            langste_boven = boven

        vorig_priem = num

print(f"Resultaat: {langste_onder} tot {langste_boven} (lengte: {langste_reeks})")