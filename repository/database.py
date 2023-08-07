import psycopg2 as db
import os


class DatabaseConfig:
    def __init__(self):
        self.config = {
            "postgresSql": {
                "user": os.getenv('user'),
                "password": os.getenv('password'),
                "host": os.getenv('host'),
                "port": os.getenv('port'),
                "database": os.getenv('database')
            }
        }


class Connection(DatabaseConfig):
    def __init__(self):
        DatabaseConfig.__init__(self)
        try:
            self.connec = db.connect(**self.config["postgresSql"])
            self.cur = self.connec.cursor()
        except Exception as e:
            print("Erro ao tentar conectar: ", e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.connec

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()






# realizar integração com a classe cliente
# conexao = Database()
# cliente = {"cpf": "867.478.156-02"}
# conexao.select(cliente)
