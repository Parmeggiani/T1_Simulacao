

class Filas:

    def __init__(self, ocupantes, capacidade):
        self.ocupantes = ocupantes
        self.capacidade = capacidade
        self.lista = []
        for _ in range(capacidade):
            self.lista.append(0)

    def getOcupantes(self):
        return self.ocupantes

    def getCapacidade(self):
        return self.capacidade

    def atualizaTempo(self, index, elem):
        self.lista[index] += elem

    def addOcupante(self):
        self.ocupantes = self.ocupantes + 1

    def subOcupante(self):
        self.ocupantes = self.ocupantes - 1

    def printLista(self):
        print(self.lista)