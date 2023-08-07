from report.relatorio import obterDadosDaAcao
from repository.order_db import OrderDB
from utils.cpf_validation import cpfValidator
from utils.ticker_validation import tickerValidator


class Relatorio:
    def __init__(self):
        self.cliente = None
        self.acao = None
        self.database = OrderDB()

    def pesquisarAcao(self):
        self.acao = tickerValidator() + ".SA"
        nome_arquivo = "Relatório " + self.acao + ".txt"
        obterDadosDaAcao(self.acao, nome_arquivo)

    def relatorioCarteira(self):
        self.cpf = cpfValidator()
        self.cliente = {
            'cpf': self.cpf
        }
        tickets = self.database.search(self.cliente)
        if len(tickets) == 0:
            print("Cliente não possui ações.")
            return

        for ticket in tickets:
            self.acao = str(ticket).replace("('", "").replace("',)", "")
            nome_arquivo = "Relatório " + self.acao + ' CPF ' + self.cpf + '.txt'
            obterDadosDaAcao(self.acao, nome_arquivo)
