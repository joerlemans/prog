def is_correct(ans: int or str) -> bool:
    if ans == 42 or ans == "tweeenveertig" or ans == "tweeënveertig":
        return True
    else:
        return False

if __name__ == '__main__':
    ans = str(input("Wat is het antwoord op de grote vraag van het leven, het universum en alles daarbij?"))
    result = is_correct(ans)
    if result == True:
        print("Ja")
    else:
        print("Nee")