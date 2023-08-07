import re

def rgValidator():

    validatedRg = r'^\d{2}\.\d{3}\.\d{3}-[0-9A-Za-z]$'

    while True:
        rg = input("RG:")

        if re.match(validatedRg, rg):
            return rg
        else:
            print("RG inválido! Tente novamente: ")
