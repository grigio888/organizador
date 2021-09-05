import os, sys
sys.path.insert(0, './')

from dependencias.database import FerramentaDatabase

class Esqueleto():
    def __init__(self):
        self.auto_iniciar()
        self.tabela = 'teste'
        self.resposta = ''

    def auto_iniciar(self):
        self.database = FerramentaDatabase()

    def cadastrar(self, lista_valores):
        try:
            tratado = ''

            for item in lista_valores:
                if item == lista_valores[len(lista_valores) - 1]: tratado = tratado + f'"{item}"'
                else: tratado = tratado + f'"{item}", '
            
            comando = f'insert into {self.tabela} values ({tratado})'
            self.database.executando(comando)
            self.resposta = True
        except:
            self.resposta = False

    def exibir(self, itens, lista_local, item_especifico = False):
        try:
            comando = f'select {itens} from {self.tabela}'

            if item_especifico: comando = f'{comando} where {lista_local[0]} = {lista_local[1]}'

            self.database.executando(comando, True)
            self.resposta = True
            return self.database.executando(comando, True, True)
        except:
            self.resposta = False

    def atualizar(self, dict_valores, lista_local):
        try:
            for item in dict_valores.keys():
                comando = f'update {self.tabela} set {item} = "{dict_valores[item]}" where {lista_local[0]} = {lista_local[1]}'
                self.database.executando(comando)
            self.resposta = True
        except:
            self.resposta = False

    def remover(self, lista_local):
        try:
            comando = f'delete from {self.tabela} where {lista_local[0]} = {lista_local[1]})'
            self.database.executando(comando)
            self.resposta = True
        except:
            self.resposta = False

class TratandoLogin(Esqueleto):
    def __init__(self):
        self.auto_iniciar()
        self.tabela = 'login'

class TratandoCliente(Esqueleto):
    def __init__(self):
        self.auto_iniciar()
        self.tabela = 'cliente'

class TratandoServicos(Esqueleto):
    def __init__(self):
        self.auto_iniciar()
        self.tabela = 'servico'

class TratandoItens(Esqueleto):
    def __init__(self):
        self.auto_iniciar()
        self.tabela = 'itens'

class TratandoOrcamento(Esqueleto):
    def __init__(self):
        self.auto_iniciar()
        self.tabela = 'itens'

if __name__ == '__main__':

    teste = TratandoLogin()

    valores_a_atualizar = {
        'login' : 'administrator',
        'senha' : '123456789'
    }
    
    teste.atualizar(valores_a_atualizar, ['login', f'"{teste.exibir("rowid, *", "")[0][1]}"'])

    print(teste.exibir('rowid, *', ''))
