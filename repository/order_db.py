from repository.database import Connection


class OrderDB(Connection):
    def __int__(self):
        Connection.__init__(self)

    def search(self, cliente):
        print("Buscando ordem...")
        try:
            sql_search = "SELECT ordem.ticket FROM cliente, ordem where cliente.id = ordem.cliente_id AND cliente.cpf='" + cliente['cpf'] + "';"
            tickers = self.query(sql_search)

            return tickers
        except Exception as e:
            print("Erro ao buscar ações do cliente informado: ", e)
            return False, "Erro ao buscar ações"

    def insert(self, atributos):
        print('Inserindo ordem de compra...')
        try:
            sql_insert = "INSERT INTO ordem (nome, ticket, valor_compra, quantidade_compra," \
                         "data_compra, cliente_id)" \
                         "VALUES (%s, %s, %s, %s, %s, %s)"

            values = (
                atributos['nome'],
                atributos['ticket'],
                atributos['valor_compra'],
                atributos['quantidade_compra'],
                atributos['data_compra'],
                atributos['cliente_id']
            )
            self.cur.execute(sql_insert, values)
            self.connec.commit()
            return True, "Ordem registrada com sucesso!"
        except Exception as e:
            print("Erro ao registar ordem: ", e)
            return False, "Erro ao registar ordeme"



# teste localhost para funcionamento do método "insert"
# if __name__ == "__main__":
#     order = OrderDB()
#     ordem = {
#         "nome": "Tauros armas",
#         "ticket": "TASA4",
#         "valor_compra": "12.22",
#         "quantidade_compra": "15",
#         "data_compra": "2002-02-02",
#         "cliente_id": "1",
#     }
#     success, message = order.insert(ordem)
#     if success:
#         print(message)
#     else:
#         print("Erro:", message)
