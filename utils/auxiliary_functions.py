def returnMainMenu():
    answer = input("Deseja retornar ao menu principal? (sim/não)")
    if answer == "sim":
        returnMain = True
    elif answer == "nao":
        returnMain = False
    return returnMain