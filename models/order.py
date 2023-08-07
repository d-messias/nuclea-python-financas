from repository.order_db import OrderDB
from utils.cpf_validation import cpfValidator
from utils.date_validation import validaDataCompra
from utils.ticker_validation import tickerValidator


class Order:
    def __init__(self):
        self.cliente = None
        self.atributos = None
        self.database = OrderDB()

    def cadastrarOrdem(self):
        self.cliente = input("Cliente ID: ")
        self.atributos = {
            "cliente_id": self.cliente,
            "nome": input("Nome da Ação: "),
            "ticket": tickerValidator()+".SA",
            "valor_compra": input("Valor da compra: "),
            "quantidade_compra": input("Quantidade da compra: "),
            "data_compra": validaDataCompra(),

        }
        self.database.insert(self.atributos)

    def consultarOrdem(self):
        self.cpf = cpfValidator()
        self.cliente = {
            'cpf': self.cpf
        }
        self.database.search(self.cliente)
