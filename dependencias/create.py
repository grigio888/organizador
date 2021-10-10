import sys
sys.path.insert(0, './')

import datetime, random, string
from dependencias.models_peewee import *

#tabela login
login_1 = PeeweeLogin.create(login="grigio888",senha='kiju1475',ultimo_login=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),nome_utilizador='Vinicius',endereco_utilizador='asdsd')
login_2 = PeeweeLogin.create(login="phzsantos",senha='esmerilhando',ultimo_login=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),nome_utilizador='Paulo',endereco_utilizador='asdsd')
login_3 = PeeweeLogin.create(login="llemons",senha='123456789',ultimo_login=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"),nome_utilizador='Emows',endereco_utilizador='asdsd')

#tabela cliente
cliente_1 = PeeweeCliente.create(nome="Teste",identidade=123456,endereco="vila velha",tel_1="123-456",tel_2="654-321")

cliente_2 = PeeweeCliente.create(nome="Teste2",identidade=132456,endereco="vila velha",tel_1="132-456",tel_2="645-321")

#tabela protudo, tipo 0 produto
produto_1 =  PeeweeProduto.create(nome="Tinta",tipo=0,preco=2350) #R$ 23,50
produto_2 =  PeeweeProduto.create(nome="Escada",tipo=0,preco=15260) #R$ 152,60
#tipo 1 servico
produto_3 =  PeeweeProduto.create(nome="Pintura por metro quadrado",tipo=1,preco=2000) #R$ 20,00


#tabela pedidos

#codigo de token aleatorio criado por sessão de abertura de orcamento

cod = token_creator(15)

pedido_1 = PeeweePedido.create(criado_por=login_2.login,criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"), modo=1, cliente=cliente_1.identidade, produto=produto_1.id, quantidade=1, codigo=cod)
pedido_2 = PeeweePedido.create(criado_por=login_2.login,criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"), modo=1, cliente=cliente_1.identidade, produto=produto_2.id, quantidade=2, codigo=cod)
pedido_3 = PeeweePedido.create(criado_por=login_2.login,criado_em=datetime.datetime.now().strftime("%Y-%m-%d-%H:%M"), modo=1, cliente=cliente_1.identidade, produto=produto_3.id, quantidade=3, codigo=cod)