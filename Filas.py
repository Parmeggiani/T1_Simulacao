

class Filas:

    def __init__(self, ocupantes, lista):
        self.ocupantes = ocupantes
        self.lista = lista
        f = []
        for _ in range(lista):
            f.append(0)

    def getOcupantes(self):
        return self.ocupantes

    def getLista(self):
        return self.lista

    def atualizaTempo(self, index, elem):
        self.lista[index] += elem

    def addOcupante(self):
        self.ocupantes = self.ocupantes + 1

    def subOcupante(self):
        self.ocupantes = self.ocupantes - 1
