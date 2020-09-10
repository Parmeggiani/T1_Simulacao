from Filas import Filas
from Agenda import Agenda
import math
import random

numero_filas = 0

filas = []

def criaFilas():
    f = open("config.txt", "r")
    numero_filas = int(f.readline())
    count=0
    while count < numero_filas:
        aux = f.readline()
        aux = aux.split(" ")
        filas.append(Filas(int(aux[0]), int(aux[1])))
        count+=1
    cal = f.readline()
    cal = cal.split(" ")
    randomicos = calcula(int(cal[0]), int(cal[1]), int(cal[2]), int(cal[3]))
    return randomicos

def main():
    randomicos = criaFilas()

    tempoAnterior = 0

    agenda = []

    agenda.append(Agenda("chegada", 3, 0))

    while(len(randomicos) > 0):
        menorTempo = math.inf
        indiceRetirada = 0
        for index in range(len(agenda)):
            if menorTempo > agenda[index].getTempo():
                menorTempo = agenda[index].getTempo()
                indiceRetirada = index
        
        valor = randomicos[0]

        if str(agenda[int(indiceRetirada)].getEvento()) == "chegada":
            filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
            tempoAnterior = agenda[indiceRetirada].getTempo()
            if filas[0].getOcupantes() < filas[0].getCapacidade():
                filas[0].addOcupante()
                if filas[0].getOcupantes() <= filas[0].getServidores():
                    Agenda.agendamentoSaida(None, agenda[indiceRetirada].getTempo(), randomicos[0])
                    agenda.append(Agenda.agendamentoSaida(None,agenda[indiceRetirada].getTempo(), randomicos[0]))
                    valor = randomicos[0]
                    randomicos.remove(valor)
            agenda.append(Agenda.agendamentoChegada(None, agenda[indiceRetirada].getTempo(), randomicos[0]))
            valor = randomicos[0]
            randomicos.remove(valor)

        if agenda[indiceRetirada].getEvento() == "saida":
            filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
            tempoAnterior = agenda[indiceRetirada].getTempo()
            filas[0].subOcupante()
            if filas[0].getOcupantes() >= filas[0].getServidores():
                agenda.append(Agenda.agendamentoSaida(None, agenda[indiceRetirada].getTempo(), randomicos[0]))
                randomicos.remove(valor)
        remove_da_agenda = agenda[indiceRetirada]
        agenda.remove(remove_da_agenda)
    
    filas[0].printLista()

# Sorteia os números pseudo-aleatórios
def calcula(x0, a, m, c):
    randomicos=[]
    count = 0
    while(count < m):
        randomico=(a * x0 + c) % m
        x0=randomico
        randomicos.append(randomico)
        count+=1
    return randomicos


main()