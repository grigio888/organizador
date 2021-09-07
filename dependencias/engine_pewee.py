from models_peewee import Login, Cliente, Pedido, Produto
import datetime

#read um registro
login = Login.get(Login.login == "Vinicius").get()
print(login.id, login.login, login.ultimo_login) 

#update
#login.author = "esmeril"
#Login.save()

#delete
#login = Login.get(Login.login == "vinicius")
#login.delete_instace()

#read varios registros
logins = Login.select()
print("\nSelecionando todas as linhas: \n")
for l in logins:
    print(l.login)

#FK demonstrativo
cliente = 'Teste'
print("tickets referentes ao pedido do cliente " + cliente)
pedido = (Pedido.select().join(Cliente, on=(Pedido.cliente == Cliente.identidade)).where(Cliente.nome == cliente))
for p in pedido:
    print(p.criado_em,p.produto.nome,p.quantidade, p.codigo)

#FK por codigo
cod = 'ZIiWbtlhGjoFJRi'
pedido = (Pedido.select().join(Produto, on=(Pedido.produto == Produto.id)).where(Pedido.codigo == cod))
for i in pedido:
    print(i.produto.nome)