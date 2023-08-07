from repository.client_db import ClientDB
from utils.cep import cepValidator
from utils.cpf_validation import cpfValidator
from utils.date_validation import dateValidator
from utils.format_text import formatName
from utils.rg_validation import rgValidator


class Client:
    def __init__(self):
        self.cliente = None
        self.cpf = None
        self.database = ClientDB()

    def cadastrarCliente(self):
        self.cliente = {
            "nome": formatName(input("Nome: ")),
            "cpf": cpfValidator(),
            "rg": rgValidator(),
            "dataNascimento": dateValidator(),
            "endereco": cepValidator(),
            "nrResidencia": input("Número da Casa: ")

        }
        resultado = self.database.insert(self.cliente)
        print(resultado)

    def consultarCliente(self):
        self.cpf = cpfValidator()
        self.cliente = {
            'cpf': self.cpf
        }
        self.database.search(self.cliente)

    def alterarCliente(self):
        self.cpf = cpfValidator()
        self.cliente = {
            "cpf": self.cpf,
            "nome": formatName(input("Nome: ")),
            "rg": rgValidator(),
            "data_nascimento": dateValidator(),
            "endereco": cepValidator(),
            "nr_residencia": input("Número da Casa: ")
        }
        self.database.update(self.cliente)

    def deletarCliente(self):
        self.cpf = cpfValidator()
        self.cliente = {
            'cpf': self.cpf
        }
        print(self.cliente)
        self.database.delete(self.cliente)

