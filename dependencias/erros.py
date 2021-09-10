# - Seção de Erros Customizados.


# -- cadastro de cliente:
class ClienteNomeNaoValido(Exception): pass

class ClienteIDNaoValido(Exception): pass

class ClienteEnderecoNaoValido(Exception): pass

class ClienteTelefoneNaoValido(Exception): pass

if __name__ == '__main__':
    raise ClienteNomeNaoValido('Nome nao e valido')