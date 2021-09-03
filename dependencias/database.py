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
            'login'     : 'login text primary key, senha text, ultimo_login integer, criado_em integer, nome_utilizador text, endereco_utilizador text',
            'cliente'   : 'id_cliente int primary key, nome text, identidade int primary key, endereco text, tel_1 integer, tel_2 integer',
            'servico'   : 'id_cliente int, id_pedido integer primary key, modo integer, id_orcamento integer primary key, foreign key (id_cliente) references cliente (id_cliente)',
            'itens'     : 'id_item integer primary key autoincrement, nome text, preco integer',
            'orcamento' : 'id_orcamento integer, item integer, data integer, foreign key (id_orcamento) references pedido (id_orcamento), foreign key (item) references itens (id_item)',
        }

        for item in relacao.keys():
            self.executando(f'create table if not exists {item} ({relacao[item]})')

#  TODO: 

if __name__ == "__main__":

    db = FerramentaDatabase(True)
    #db.executando(f'select name from sqlite_master where type = "table"', True)
    #print(db.resultado)
    

    #db.executando(f'insert into login values ("admin", "admin", "00000000000", "00000000000", "administrator", "nowhere")')
    #db.executando('insert into cliente values ("Angolano", "Angola", "5527998881234", "0")')
    #db.executando('insert into itens values ("1000", "Troca de Algo", 15000)')
    
    #db

    #print(db.executando('select * from login', True, True))
    #db.executando('delete from login')