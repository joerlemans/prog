def is_correct(ans: int,str) -> bool:
    if ans == 42 or ans == "tweeenveertig" or ans == "tweeënveertig":
        return True
    else:
        return False

if __name__ == '__main__':
    ans = input("Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?")