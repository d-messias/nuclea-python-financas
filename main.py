from models.order import Order
from models.client import Client
from models.relatorio import Relatorio

dadosClientes = []

def main():
    validador = True
    while validador:
        print("Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma opção abaixo:")
        print("1 - Cliente"
              "\n2 - Ordem."
              "\n3 - Realizar análise da carteira."
              "\n4 - Gerar relatórios."
              "\n5 - Sair.")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            cliente = Client()
            print("Menu de gerenciamento dos dados do cliente: ")
            print("1 - Cadastrar Cliente."
                  "\n2 - Consultar Cliente."
                  "\n3 - Alterar Cliente."
                  "\n4 - Excluir Cliente."
                  "\n5 - Voltar ao menu principal.")
            opcao_menu_cliente = input("Digite a opção desejada: ")

            if opcao_menu_cliente == "1":
                cliente.cadastrarCliente()
            elif opcao_menu_cliente == "2":
                cliente.consultarCliente()
            elif opcao_menu_cliente == "3":
                cliente.alterarCliente()
            elif opcao_menu_cliente == "4":
                cliente.deletarCliente()
            else:
                print("Retornando ao menu principal...")

        elif opcao == "2":
            print("Menu de gerenciamento de Ordens.")
            print("1 - Cadastrar ordem.")
            print("2 - Voltar ao menu principal.")
            opcao_menu_ordem = input("Digite a opção desejada: ")
            if opcao_menu_ordem == "1":
                acao = Order()
                acao.cadastrarOrdem()
            else:
                print("Retornando ao menu principal...")


        elif opcao == "3":
            print("Menu de Análise de Carteira.")
            print("1 - Consultar carteira por CPF.")
            print("2 - Voltar ao menu principal.")
            opcao_menu_analise = input("Digite a opção desejada: ")
            if opcao_menu_analise == "1":
                acao = Order()
                acao.consultarOrdem()
            else:
                print("Retornando ao menu principal...")

        elif opcao == "4":
            acao = Relatorio()
            print("Bem vindo ao menu de Relatório. Selecione uma das opções abaixo:")
            print("1 - Pesquisar ação por ticket.")
            print("2 - Consultar relatório da carteira por CPF.")
            print("3 - Voltar ao menu principal.")
            opcao_menu_relatorio = input("Digite a opção desejada: ")
            if opcao_menu_relatorio == "1":
                acao.pesquisarAcao()
            elif opcao_menu_relatorio == "2":
                acao.relatorioCarteira()
            else:
                print("Retornando ao menu principal...")
        elif opcao == "5":
            print("Obrigado por utilizar o sistema de gerenciamento de carteira de ações da Nuclea. Até a próxima!")
            validador = False
        else:
            print("Opção inválida. Tente novamente.")



main()


