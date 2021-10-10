import sys
sys.path.insert(0, './')

import datetime
from dependencias.models_peewee import *

#read um registro
cliente = PeeweeCliente.get(PeeweeCliente.nome == "Hermione Granger")
#print([cliente.nome, cliente.identidade])
#print(cliente.id)

produto = PeeweeProduto.select()
for t in produto:
    print(t.nome)

#update
#login.author = "esmeril"
#Login.save()

#delete
#login = Login.get(Login.login == "vinicius")
#login.delete_instace()

##read varios registros
#logins = Login.select()
#print("\nSelecionando todas as linhas: \n")
#for l in logins:
#    print(l.login)

##FK demonstrativo
#cliente = 'Teste'
#print("tickets referentes ao pedido do cliente " + cliente)
#pedido = (Pedido.select().join(Cliente, on=(Pedido.cliente == Cliente.identidade)).where(Cliente.nome == cliente))
#for p in pedido:
#    print(p.criado_em,p.produto.nome,p.quantidade, p.codigo)
#
##FK por codigo
#cod = 'ZIiWbtlhGjoFJRi'
#pedido = (Pedido.select().join(Produto, on=(Pedido.produto == Produto.id)).where(Pedido.codigo == cod))
#for i in pedido:
#    print(i.produto.nome)