class Filas:

    def __init__(self, servidores, capacidade):
        if capacidade == 0:
            capacidade = 100000
        self.capacidade = capacidade
        self.servidores = servidores
        self.ocupantes = 0
        self.lista = []
        for _ in range(capacidade+1):
            self.lista.append(0)

    def getOcupantes(self):
        return self.ocupantes

    def getCapacidade(self):
        return self.capacidade

    def getServidores(self):
        return self.servidores

    def getLista(self):
        return self.lista

    def atualizaTempo(self, index, elem):
        self.lista[index] += elem

    def addOcupante(self):
        self.ocupantes = self.ocupantes + 1

    def subOcupante(self):
        self.ocupantes = self.ocupantes - 1

    def printLista(self):
        print("TEMPOS DA FILA ===> ",self.lista)