def convert(text: str) -> str:
    """
    convert snake naar camel
    
    >>> convert("twee_woorden")
    'tweeWoorden'
    """
    cam = ""
    snake = False
    for i in text:
        if snake == True:
            cam = cam + i.upper()
            snake = False
        if i == "_":
            snake = True
        if snake == False:
            cam = cam + i
        
        
    return cam