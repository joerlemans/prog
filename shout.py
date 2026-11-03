def shout(text: str) -> str:
    """
    schrijft alle woorden in hoofdletters
    
    >>> shout("hoi")
    'HOI'
    """
    caps = ""
    for i in text:
        caps = caps + i.upper()
    return caps

if __name__ == '__main__':
    result =