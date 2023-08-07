import requests
import re


def searchCep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if "erro" not in data:
            adress = {
                "CEP": re.sub(r'[\W_]+', '', data['cep']),
                "Logradouro": data['logradouro'],
                "Complemento": data['complemento'],
                "Bairro": data['bairro'],
                "Cidade": data['localidade'],
                "Estado": data['uf']
            }
            return adress


def cepValidator():
    while True:
        cep = input("CEP: ")
        if cep.isdigit() and len(cep) == 8:
            cepReturned = searchCep(cep)
            if cepReturned:
                return cepReturned
        else:
            print("CEP inválido! Tente novamente. ")


if __name__ == "__main__":
    cepValidator()
