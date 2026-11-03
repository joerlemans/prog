def yell(text: str) -> str:
    """
    maakt een nieuwe string met dubbel ! en ?
    
    >>> yell("Hey!")
    Hey!!
    
    >>> yell("Wat?!")
    Wat!!??
    
    >>> yell("ieufhiweufl..,/")
    ieufhiweufl..,/
    
    """
    result = ""
    for i in text:
        if i in "!?":
           result = result + i + i
        else:
            result = result + i
    