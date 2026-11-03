def shout(text: str) -> str:
    """
    schrijft alle woorden in hoofdletters
    
    >>> shout("hoi")
    'HOI'
    
    >>> shout("hahaha!!")
    'HAHAHA!!'
    """
    caps = ""
    for i in text:
        caps = caps + i.upper()
    return caps

if __name__ == '__main__':
    result = input()
    print(shout(result))