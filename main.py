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
        for index in range(len(agenda)):
            if menorTempo > agenda[index].getTempo():
                menorTempo = agenda[index].getTempo()
                indiceRetirada = index

        print("Indice ", indiceRetirada)
        print("ESTOU AQUI ====> ", agenda[int(indiceRetirada)].getEvento())
        
        valor = randomicos[0]

        if str(agenda[int(indiceRetirada)].getEvento()) == "chegada":
            aux_fila = filas[selecionaFila(numero_filas)]
            aux_fila.atualizaTempo(aux_fila.getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
            tempoAnterior = agenda[indiceRetirada].getTempo()
            if aux_fila.getOcupantes() < aux_fila.getCapacidade():
                aux_fila.addOcupante()
                if aux_fila.getOcupantes() <= 1:
                    print("BATMAN ",agenda[indiceRetirada].getTempo())
                    Agenda.agendamentoSaida(None, agenda[indiceRetirada].getTempo(), randomicos[0])
                    agenda.append(Agenda.agendamentoSaida(None,agenda[indiceRetirada].getTempo(), randomicos[0]))
                    valor = randomicos[0]
                    randomicos.remove(valor)
            agenda.append(Agenda.agendamentoChegada(None, agenda[indiceRetirada].getTempo(), randomicos[0]))
            randomicos.remove(valor)

        if agenda[indiceRetirada].getEvento() == "saida":
            aux_fila = filas[selecionaFila(numero_filas)]
            aux_fila.atualizaTempo(aux_fila.getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
            tempoAnterior = agenda[indiceRetirada].getTempo()
            aux_fila.subOcupante()
            if aux_fila.getOcupantes() >= 1:
                agenda.append(Agenda.agendamentoSaida(None, agenda[indiceRetirada].getTempo(), randomicos[0]))
                randomicos.remove(valor)
        remove_da_agenda = agenda[indiceRetirada]
        agenda.remove(remove_da_agenda)

def selecionaFila(numero_filas):
    return random.randint(0,numero_filas)

# Sorteia os números pseudo-aleatórios
def calcula(x0, a, m, c):
    randomicoss=[]
    for index in range(m):
        randomicos=(a * x0 + c) % m
        x0=randomicos
        randomicoss.append(randomicos)
    return randomicoss


main()