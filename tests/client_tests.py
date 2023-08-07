import unittest
from unittest.mock import patch

from faker import Faker

from main import main, dadosClientes
from utils.cpf_validation import gera_cpf


class TestClients(unittest.TestCase):

    def gerarNomeFake(self):
        fake = Faker()
        return fake.name()

    def testCliente(self):
        nome = self.gerarNomeFake()
        cpf = gera_cpf()
        inputs = ["1","1", nome, cpf, "12.345.678-x", "02/02/2002", "50781290", "45", "nao"]

        with patch("builtins.input", side_effect = inputs):
            main()

        expectedClient = {
            "nome": nome,
            "cpf": f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}",
            "rg": "12.345.678-x",
            "dataNascimento": "02/02/2002",
            "endereco": {"CEP": "50781290",
                         "Logradouro": "Rua Barros Sobrinho",
                         "Bairro": "Areias",
                         "Cidade": "Recife",
                         "Estado": "PE"},
            "nrResidencia": "45",
        }

        self.assertIn(expectedClient, dadosClientes)
