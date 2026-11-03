def convert(text: str) -> str:
    """
    convert snake naar camel
    
    >>> convert("twee_woorden")
    'tweeWoorden'
    
    >>> convert("hi_hoi_bye")
    'hiHoiBye'
    """
    cam = ""
    snake = False
    for i in text:
        if snake == True:
            cam = cam + i.upper()
            snake = False
        elif i == "_":
            snake = True
        elif snake == False:
            cam = cam + i
    return cam
    
    snake = ""
    for i in text:
        if i.isupper == True:
            snake = snake + "_"
        
        

if __name__ == '__main__':
    result = print()