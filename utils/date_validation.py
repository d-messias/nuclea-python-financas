from datetime import datetime

def dateValidator():
    while True:
        birthDate = input("Data Nascimento: ")

        try:
            formatedDate = datetime.strptime(birthDate, "%d/%m/%Y").date()
            nowDate = datetime.now().date()

            if formatedDate < nowDate:
                return formatedDate.strftime("%d/%m/%Y")
            else:
                print("A data não pode ser maior que a data de Hoje.")
        except ValueError:
            print("Erro! Data inválida. Tente novamente.")


def validaDataCompra():

    while True:
        valida_data_compra = input("Data de compra: ")

        try:
            data_convertida = datetime.strptime(valida_data_compra, "%d/%m/%Y").date()

            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("Data de compra maior que a data atual. Tente novamente: ")
        except ValueError as e:
            print(f'Data de compra inválida "{e}". Tente novamente: ')