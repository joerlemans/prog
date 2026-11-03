def convert(text: str) -> str:
    
    cam = ""
    snake = False
    for i in text:
        if i == "_":
            snake = True
            