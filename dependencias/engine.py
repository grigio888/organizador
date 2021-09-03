from database import FerramentaDatabase

class Esqueleto():
    def __init__(self):
        self.auto_iniciar()
        self.tabela = 'teste'

    def auto_iniciar(self):
        self.database = FerramentaDatabase()

    def cadastrar(self, lista_valores):
        tratado = ''

        for item in lista_valores:
            if item == lista_valores[len(lista_valores) - 1]: tratado = tratado + f'"{item}"'
            else: tratado = tratado + f'"{item}", '
        
        comando = f'insert into {self.tabela} values ({tratado})'
        self.database.executando(comando)

    def exibir(self, itens, lista_local, item_especifico = False):
        comando = f'select {itens} from {self.tabela}'

        if item_especifico: comando = f'{comando} where {lista_local[0]} = {lista_local[1]}'

        self.database.executando(comando, True)
        return self.database.executando(comando, True, True)

    def atualizar(self, dict_valores, lista_local):
        valores = [f'{item} = {dict_valores[item]}' for item in dict_valores.keys()]
        for item in valores:
            comando = f'update {self.tabela} values ({valores}) where {lista_local[0]} = {lista_local[1]}'
        self.database.executando(comando)

    def remover(self, lista_local):
        comando = f'delete from {self.tabela} where {lista_local[0]} = {lista_local[1]})'
        self.database.executando(comando)

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

    teste = TratandoCliente()
    #teste.atualizar(['Macaco', 'Floresta', '552233226655', '552233665511'])
    print(teste.exibir('rowid, *', ''))