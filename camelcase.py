def convert(text: str) -> str:
    """
    convert snake naar camel
    
    >>> convert("twee_woorden")
    'tweeWoorden'
    
    >>> convert("hiHoi_bye")
    'hi_hoi_bye'
    """
    snake = ""
    for i in text:
        if i.isupper == True:
            snake = snake + "_"
        snake = snake + i
    return snake
        

if __name__ == '__main__':
    result = print()