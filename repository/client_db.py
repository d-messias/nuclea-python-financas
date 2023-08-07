from repository.database import Connection


class ClientDB(Connection):
    def __int__(self):
        Connection.__init__(self)

    def search(self, cliente):
        print("Buscando cliente...")
        try:
            sql_search = "SELECT * FROM cliente where cpf ='" + cliente['cpf'] + "';"
            clientes = self.query(sql_search)
            for cliente in clientes:
                print(cliente)
            if len(clientes) == 0:
                print("Esse cliente não existe.")
            return clientes

        except Exception as e:
            print("Erro ao buscar cliente: ", e)
            return False, "Erro ao buscar cliente"

    def insert(self, cliente):
        print('Inserindo cliente...')
        try:
            sql_insert = "INSERT INTO cliente (nome, cpf, rg, data_nascimento, cep, logradouro," \
                         "complemento, bairro, cidade, " \
                         "estado, nr_residencia)" \
                         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            values = (
                cliente['nome'],
                cliente['cpf'],
                cliente['rg'],
                cliente['data_nascimento'],
                cliente['cep'],
                cliente['logradouro'],
                cliente['complemento'],
                cliente['bairro'],
                cliente['cidade'],
                cliente['estado'],
                cliente['nr_residencia']
            )
            self.cur.execute(sql_insert, values)
            self.connec.commit()
            return True, "Cliente cadastrado com sucesso!"
        except Exception as e:
            print("Erro ao Inserir cliente: ", e)
            return False, "Erro ao Inserir cliente"

    def delete(self, cliente):
        try:
            sql_search = "SELECT * FROM cliente WHERE cpf = %s"
            if not self.query(sql_search, (cliente['cpf'],)):
                return "Não foi possível encontrar o cliente com este CPF"
            sql_delete = f"DELETE FROM cliente WHERE cpf = %s"
            self.execute(sql_delete, (cliente['cpf'],))
            self.commit()
            return True, "Cadastro do cliente deletado com sucesso!"
        except Exception as e:
            print("Erro ao deletar cliente: ", e)
            return False, "Erro ao deletar cliente"

    def update(self, cliente):
        try:
            sql_search = "SELECT * FROM cliente WHERE cpf = %s"
            if not self.query(sql_search, (cliente['cpf'],)):
                return False, "Não foi possível encontrar o cliente com este CPF"

            sql_update = "UPDATE cliente SET nome = %s, rg = %s, data_nascimento = %s, cep = %s, logradouro = %s, " \
                         "complemento = %s, bairro = %s, cidade = %s, estado = %s, nr_residencia = %s WHERE cpf = %s"
            values = (
                cliente['nome'],
                cliente['rg'],
                cliente['data_nascimento'],
                cliente['cep'],
                cliente['logradouro'],
                cliente['complemento'],
                cliente['bairro'],
                cliente['cidade'],
                cliente['estado'],
                cliente['nr_residencia'],
                cliente['cpf']
            )
            self.execute(sql_update, values)
            self.commit()

            return True, "Cadastro atualizado com sucesso!"
        except Exception as e:
            print("Erro ao atualizar cliente: ", e)
            return False, "Erro ao atualizar cliente"

# teste localhost para funcionamento do método "insert"
# if __name__ == "__main__":
#     client = ClientDB()
#     cliente = {
#         "nome": "Jorge",
#         "cpf": "398.060.394-37",
#         "rg": "32.445.679-x",
#         "data_nascimento": "2002-02-02",
#         "cep": "50781290",
#         "logradouro": "Rua Barros Sobrinho",
#         "complemento": "n/a",
#         "bairro": "Areias",
#         "cidade": "Recife",
#         "estado": "PE",
#         "nr_residencia": "45"
#     }
#     success, message = client.insert(cliente)
#     if success:
#         print(message)
#     else:
#         print("Erro:", message)


# teste localhost para funcionamento do método "update"
# if __name__ == "__main__":
#     client = ClientDB()
#     success, message = client.update("Daniel Messias da Silva", "12.345.678-x", "2002-02-02", "50781290", "Rua Barros Sobrinho",
#                                      "n/a", "Areias", "Recife", "PE", "45", "867.478.156-02")
#     if success:
#         print(message)
#     else:
#         print("Erro:", message)


# if __name__ == "__main__":
#     client = ClientDB()
#     success, message = client.delete("098.060.394-37")
#
#     if success:
#         print(message)
#     else:
#         print("Erro:", message)
