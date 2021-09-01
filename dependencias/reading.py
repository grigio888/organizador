import datetime

class Lendo():
    def __init__(self):
        self.data = datetime.datetime.now()

    def lendo(self, arquivo):
        lendo = open(arquivo, 'r', encoding='utf-8')
        result = lendo.readlines()
        return result

    def gravando(self, arquivo, texto):
        gravando = open(arquivo, 'a', encoding='utf-8')
        gravando.write(texto)
        gravando.close

if __name__ == '__main__':

    pass
