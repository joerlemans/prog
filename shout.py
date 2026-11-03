def shout(text: str) -> str:
    """
    schrijft alle woorden in hoofdletters
    
    >>> shout("hoi")
    'HOI'
    """
    caps = ""
    for i in text:
        caps = cap + i.upper()
    return caps