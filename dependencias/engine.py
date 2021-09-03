from database import FerramentaDatabase

class Esqueleto():
    def __init__(self):
        self.database = FerramentaDatabase()
        self.tabela = 'teste'

    def cadastrar(self, tabela, lista_valores):
        comando = f'insert into {self.tabela} values ({lista_valores})'
        self.database.executando(comando)

    #def exibir(self, itens, item_especifico = False, lista_local):
    #    comando = f'select {itens} from {self.tabela}'
    #    if item_especifico: comando = f'{comando} where {lista_local[0]} = {lista_local[1]}'
    #    self.database.executando(comando, True)
    #    return self.database.executando(comando, True, True)

    def exibir(self):
        pass

    def atualizar(self, dict_valores, lista_local):
        valores = [f'{item} = {dict_valores[item]}' for item in dict_valores.keys()]
        for item in valores:
            comando = f'update {self.tabela} values ({valores}) where {lista_local[0]} = {lista_local[1]}'
        self.database.executando(comando)

    def remover(self, lista_local):
        comando = f'delete from {self.tabela} where {lista_local[0]} = {lista_local[1]})'
        self.database.executando(comando)


class CuidadosCliente(Esqueleto):
    def __init__(self):
        super().__init__()

#class CRUD_Organizador():
#
#    #clientes
#
#    def cadastrar_cliente(self):
#
#    def listar_clientes(self, id):
#        #se o id for informado, buscar especifico
#
#    def atualizar_cliente(self):
#
#    def remover_cliente(self):
#
#    #conta_login
#
#    def cadastrar_conta(self):
#    def listar_contas(self, id):
#        #se o id for informado, buscar especifico
#    def atualizar_conta(self):
#    def remover_conta(self):
#
#    #servicos
#
#    def cadastrar_servico(self):
#    def listar_servicos(self, id):
#    def atualizar_servicos
#    
