#testes unitarios banco
import os, sys
sys.path.insert(0, './')

from dependencias.engine import *
import unittest


class DatabaseCrudIteractions(unittest.TestCase):

    def setUp(self):
        self.saida = False
        #tabelas
        self.login = TratandoLogin()
        self.cliente = TratandoCliente()
        self.servicos = TratandoServicos()
        self.itens = TratandoItens()
        self.orcamento = TratandoOrcamento()
        self.lista_logins = []

    #Testes na tabela login

    def test_cadastro_login(self):
        self.login.cadastrar(["admin2", "admi2n", "00000012000","00000000000", "administrator", "nowhere"])
        self.assertTrue(self.login.resposta)

    def test_exibir_logins(self):
        self.login.exibir('rowid, *', '')  #  [(1, 'admin', 'admin', 0, 0, 'administrator', 'nowhere'), (2, 'admin2', 'admi2n', 12000, 0, 'administrator', 'nowhere')]
        self.assertTrue(self.login.resposta)

    def test_atualizar_login(self):
        dado = self.login.exibir('rowid, *', '')[0][1]
        valores_a_atualizar = {
            'login' : 'teste',
            'senha' : '123456789'
        }
        self.login.atualizar(valores_a_atualizar, ['login', f'{dado}'])
        self.assertTrue(self.login.resposta)

    #def remover_login

    #TODO: tabelas cliente, pedido, produto

if __name__ == "__main__":
    
    unittest.main()
