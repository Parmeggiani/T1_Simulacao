from Filas import Filas
from Agenda import Agenda
import math
import random

numero_filas = 0

filas = []

def criaFilas():
    f = open("config.txt", "r")
    numero_filas = int(f.readline())
    for index in range(numero_filas):
        aux = f.readline()
        aux = aux.split(" ")
        filas.append(Filas(int(aux[0]),int(aux[1])))
    cal = f.readline()
    cal = cal.split(" ")
    randomicos = calcula(int(cal[0]), int(cal[1]), int(cal[2]), int(cal[3]))
    return randomicos

def main():
    randomicos = criaFilas()

    tempoAnterior = 0

    agenda = []

    agenda.append(Agenda("chegada", 10, 0))

    while(len(randomicos) > 0):
        menorTempo = math.inf
        indiceRetirada = 0
        for index in agenda:
            if menorTempo > index.getTempo():
                menorTempo = index.getTempo()
                indiceRetirada = index

        if str(agenda[int(indiceRetirada)].getEvento()) == "chegada":
            aux_fila = filas[selecionaFila(numero_filas)]
            aux_fila.atualizaTempo(aux_fila.getOcupantes(), index.getTempo() - tempoAnterior)
            tempoAnterior=index.getTempo()
            if aux_fila.getOcupantes < aux_fila.getCapacidade():
                aux_fila.addOcupante()
                if aux_fila.getOcupantes() <= 1:
                    agenda.append(Agenda.agendamentoSaida(index.getTempo(), randomicos[0]))
                    randomicos.remove(0)
            agenda.append(Agenda.agendamentoChegada(index.getTempo(), randomicos[0]))
            randomicos.remove(0)

        if agenda[indiceRetirada].getEvento() == "saida":
            aux_fila = filas[selecionaFila(numero_filas)]
            aux_fila.atualizaTempo(aux_fila.getOcupantes(), index.getTempo() - tempoAnterior)
            tempoAnterior=index.getTempo()
            aux_fila.subOcupante()
            if aux_fila.getOcupantes() >= 1:
                agenda.append(Agenda.agendamentoSaida(index.getTempo(), randomicos[0]))
                randomicos.remove(0)
        randomicos.remove(indiceRetirada)

def selecionaFila(numero_filas):
    return random.randint(0,numero_filas-1)

# Sorteia os números pseudo-aleatórios
def calcula(x0, a, m, c):
    randomicoss=[]
    for index in range(m):
        randomicos=(a * x0 + c) % m
        x0=randomicos
        randomicoss.append(randomicos)
    return randomicoss


main()