def convert(text: str) -> str:
    """
    convert snake naar camel
    
    >>> convert("tweeWoorden")
    'twee_woorden'
    
    >>> convert("hiHoiBye")
    'hi_hoi_bye'
    """
    snake = ""
    for i in text:
        if i in "QWERTYUIOPASDFGHJKLZXCVBNM":
            print("l")
            snake = snake + "_"
        snake = snake + i.lower()
    return snake

if __name__ == '__main__':
    result = input()
    print(convert(result))