def convert(text: str) -> str:
    
    cam = ""
    snake = False
    for i in text:
        if snake == True:
            cam
        if i == "_":
            snake = True
        if snake == False:
            cam = cam + i
        