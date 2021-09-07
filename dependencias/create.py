import datetime, random, string
from models_peewee import *

#tabela login
login_1 = Login.create(login="Vinicius",senha='Teste',ultimo_login=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),nome_utilizador='teste',endereco_utilizador='asdsd')

login_2 = Login.create(login="Esmeril",senha='Teste',ultimo_login=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),nome_utilizador='teste',endereco_utilizador='asdsd')

#tabela cliente
cliente_1 = Cliente.create(nome="Teste",identidade=123456,endereco="vila velha",tel_1="123-456",tel_2="654-321")

cliente_2 = Cliente.create(nome="Teste2",identidade=132456,endereco="vila velha",tel_1="132-456",tel_2="645-321")

#tabela protudo, tipo 0 produto
produto_1 =  Produto.create(nome="Tinta",tipo=0,preco=2350) #R$ 23,50
produto_2 =  Produto.create(nome="Escada",tipo=0,preco=15260) #R$ 152,60
#tipo 1 servico
produto_3 =  Produto.create(nome="Pintura por metro quadrado",tipo=1,preco=2000) #R$ 20,00


#tabela pedidos

#codigo de token aleatorio criado por sessão de abertura de orcamento
def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters)for i in range(length))
    return result_str

cod = get_random_string(15)

pedido_1 = Pedido.create(criado_por=login_2.login,criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),cliente=cliente_1.identidade, produto=produto_1.id, quantidade=1, codigo=cod)
pedido_2 = Pedido.create(criado_por=login_2.login,criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),cliente=cliente_1.identidade, produto=produto_2.id, quantidade=2, codigo=cod)
pedido_3 = Pedido.create(criado_por=login_2.login,criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),cliente=cliente_1.identidade, produto=produto_3.id, quantidade=3, codigo=cod)