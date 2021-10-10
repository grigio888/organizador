import peewee
import datetime
import random
import string

db = peewee.SqliteDatabase('dependencias/database.db')

def token_creator(length):
    result_str = ''.join(random.choice(string.ascii_letters)for i in range(length))
    return result_str

#tabelas login, cliente, pedido, produtos, produtos_do_pedido

class BaseModel(peewee.Model):

    class Meta:
        database=db


class PeeweeLogin(BaseModel):

    login = peewee.CharField(unique=True)
    senha = peewee.CharField()
    ultimo_login = peewee.DateTimeField()
    criado_em = peewee.DateTimeField()
    nome_utilizador = peewee.CharField()
    endereco_utilizador = peewee.CharField()
    class Meta:
        database = db
        table_name = 'Login'


class PeeweeCliente(BaseModel):
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

class PeeweeProduto(BaseModel):
    nome = peewee.CharField()
    # 0 para material 1 para servico
    tipo = peewee.BooleanField()
    preco = peewee.IntegerField()
    class Meta:
        database = db
        table_name = 'Produto'

class PeeweePedido(BaseModel):
    #chave estrangeira tabela Login para obter nome do vendedor
    criado_por = peewee.ForeignKeyField(PeeweeLogin)
    criado_em = peewee.DateTimeField()
    modo = peewee.BooleanField()  # Pedido de compra ou orçamento.
    
    #obter nome do cliente
    cliente = peewee.ForeignKeyField(PeeweeCliente)
    produto = peewee.ForeignKeyField(PeeweeProduto)
    quantidade = peewee.IntegerField()
    observacao = peewee.TextField()
    #codigo do pedido com todos os itens cadastrados vinculados a sessão e FOR
    codigo = peewee.TextField()

    class Meta:
        database = db
        table_name = 'Pedido'

class PeeweeStatus(BaseModel):
    status = peewee.TextField()
    numero = peewee.IntegerField()

    class Meta:
        database = db
        table_name = 'Status'

class PeeweeStatusPedido(BaseModel):
    #chave estrangeira tabela Pedido
    codigo = peewee.ForeignKeyField(PeeweePedido)
    criado_por = peewee.ForeignKeyField(PeeweeLogin)
    criado_em = peewee.DateTimeField()
    concluido_em = peewee.DateTimeField()
    #status 0 - cancelado, 1 - em andamento, 2 - concluido
    status = peewee.ForeignKeyField(PeeweeStatus)  

    class Meta:
        database = db
        table_name = 'Status_pedido'

if __name__ == '__main__':

    for item in [PeeweeLogin, PeeweeCliente, PeeweePedido, PeeweeProduto, PeeweeStatus, PeeweeStatusPedido]:
        try: item.create_table()
        except peewee.OperationalError: print(f"Tabela {item} ja existe!")

    #criacao dos registros de status na criacao do banco
    list_status = ['Cancelado','Em andamento','Concluido']
    for numero,status in enumerate(list_status):
        register_status = PeeweeStatus.create(status=status,numero=numero)