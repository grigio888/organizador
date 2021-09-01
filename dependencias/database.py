import sqlite3

class FerramentaDatabase():
    def __init__(self, inicio = False):
        self.database = 'dependencias/banco/banco_de_teste.db'
        self.resultado = 0
        if inicio: self.auto_iniciar()

    def executando(self, comando, lendo = False, retornando = False):
        login = sqlite3.connect(self.database)
        cursor = login.cursor()
        executando = (comando)
        cursor.execute(executando)
        if lendo == True: self.resultado = cursor.fetchall()
        login.commit()
        login.close()
        if retornando == True: return self.resultado

    def auto_iniciar(self):
        relacao = {
            'login':'login text primary key, senha text, ultimo_login int, criado_em int, nome_utilizador text, endereco_utilizador text',
            'cliente':'nome text primary key, endereco text, tel_1 int, tel_2 int',
            'pedido':'cliente text, n_pedido int primary key, modo int, id_sacola int, foreign key (cliente) references cliente (nome)',
            'sacola':'id_sacola int primary key, '
        }

if __name__ == "__main__":

    pass