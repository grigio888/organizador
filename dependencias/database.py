import sqlite3

class FerramentaDatabase():
    def __init__(self, inicio = False):
        self.database = 'dependencias/database.db'
        self.resultado = 0
        if inicio: self.auto_iniciar()

    def executando(self, comando, lendo = False, retornando = False):
        login = sqlite3.connect(self.database)
        cursor = login.cursor()
        executando = (comando)
        cursor.execute(executando)
        if lendo: self.resultado = cursor.fetchall()
        login.commit()
        login.close()
        if retornando: return self.resultado

    def auto_iniciar(self):
        relacao = {
            'login'              : 'login text primary key, senha text, ultimo_login integer, criado_em integer, nome_utilizador text, endereco_utilizador text',
            'cliente'            : 'id_cliente integer primary key, nome text, identidade integer, endereco text, tel_1 integer, tel_2 integer',
            'pedido'             : 'id_cliente integer, id_pedido integer primary key, modo integer, foreign key (id_cliente) references cliente (id_cliente)',
            'produtos'           : 'id_produto integer primary key autoincrement, modo integer, nome text, preco integer',
            'produtos_do_pedido' : 'id_pedido integer, id_produto integer, data integer, foreign key (id_pedido) references pedido (id_pedido), foreign key (id_produto) references produto (id_produto)',
        }

        for item in relacao.keys():
            self.executando(f'create table if not exists {item} ({relacao[item]})')

#  TODO: 

if __name__ == "__main__":

    db = FerramentaDatabase(True)
    #db.executando(f'select name from sqlite_master where type = "table"', True)
    #print(db.resultado)
    

    db.executando('insert into login values ("admin", "admin", "00000000000", "00000000000", "administrator", "nowhere")')
    db.executando('insert into cliente values ("1000", "Angolano", "12345678901", "Angola", "5527998881234", "0")')
    db.executando('insert into produtos values ("1000", "01", "Troca de Algo", 15000)')
    
    #db

    #print(db.executando('select * from login', True, True))
    #db.executando('delete from login')