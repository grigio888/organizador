import peewee

db = peewee.SqliteDatabase('database.db')


#tabelas login, cliente, pedido, produtos, produtos_do_pedido

class BaseModel(peewee.Model):

    class Meta:
        database=db


class Login(BaseModel):

    login = peewee.CharField(unique=True)
    senha = peewee.CharField()
    ultimo_login = peewee.DateTimeField()
    criado_em = peewee.DateTimeField()
    nome_utilizador = peewee.CharField()
    endereco_utilizador = peewee.CharField()
    class Meta:
        database = db
        table_name = 'Login'


class Cliente(BaseModel):
    # id já é criado automaticamente
    nome = peewee.CharField()
    #cpf sem caracteres especiais
    identidade = peewee.IntegerField(unique=True)
    endereco = peewee.TextField()
    tel_1 = peewee.TextField()
    tel_2 = peewee.TextField()
    class Meta:
        database = db
        table_name = 'Cliente'

class Produto(BaseModel):
    nome = peewee.CharField()
    # 0 para material 1 para servico
    tipo = peewee.BooleanField()
    preco = peewee.IntegerField()
    class Meta:
        database = db
        table_name = 'Produto'

class Pedido(BaseModel):
    #chave estrangeira tabela Login para obter nome do vendedor
    criado_por = peewee.ForeignKeyField(Login)
    criado_em = peewee.DateTimeField()
    modo = peewee.BooleanField()  # Pedido de compra ou orçamento.
    
    #obter nome do cliente
    cliente = peewee.ForeignKeyField(Cliente)
    produto = peewee.ForeignKeyField(Produto)
    quantidade = peewee.IntegerField()
    #codigo do pedido com todos os itens cadastrados vinculados a sessão e FOR
    codigo = peewee.TextField()

    class Meta:
        database = db
        table_name = 'Pedido'

if __name__ == '__main__':

    for item in [Login, Cliente, Pedido, Produto]:
        try: item.create_table()
        except peewee.OperationalError: print(f"Tabela {item} ja existe!")