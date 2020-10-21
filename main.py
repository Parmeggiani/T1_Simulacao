from Filas import Filas
from Agenda import Agenda
import math
import random
from random import randint

numero_filas = 0

filas = []
agenda = []

def criaFilas():
    f = open("config.txt", "r")
    numero_filas = int(f.readline())
    count=0
    #execucoes=0
    media_resultados = []
    filas=[]
    while count < numero_filas:
        aux = f.readline()
        aux = aux.split(" ")
        filas.append(Filas(int(aux[0]), int(aux[1])))
        print(len(filas))
        count+=1
    cal = f.readline()
    cal = cal.split(" ")
    randomicos = calcula(int(cal[0]), int(cal[1]), int(cal[2]), int(cal[3]))
    main(randomicos,filas)
    #media_resultados.append(filas[0].getLista())
    #randomicos = [0.3276,0.8851,0.1643,0.5542,0.6813,0.7221,0.9881]
    #calculaMedia(media_resultados)
    

def main(randomicos,filas):

    tempoAnterior = 0
    agenda = []
    agenda.append(Agenda("chegada", 2, 0, 0, 0))

    while(len(randomicos) > 0):
        menorTempo = math.inf
        indiceRetirada = 0
        for index in range(len(agenda)):
            if menorTempo > agenda[index].getTempo():
                menorTempo = agenda[index].getTempo()
                indiceRetirada = index
        
        valor = randomicos[0]

        if agenda[indiceRetirada].getEvento() == "chegada":
            filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior = chegada(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior)

        if agenda[indiceRetirada].getEvento() == "saida":
            filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior = saida(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior)
        
        if agenda[indiceRetirada].getEvento() == "proximo":
            proximo(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior)

        remove_da_agenda = agenda[indiceRetirada]
        agenda.remove(remove_da_agenda)
    print("Tempo",tempoAnterior)
    filas[0].printLista()


def chegada(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    if filas[0].getOcupantes() < filas[0].getCapacidade():
        filas[0].addOcupante()
        if filas[0].getOcupantes() <= filas[0].getServidores():
            if randint(0,1) <= 0.8:
                agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 2))
            else:
                agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 3))
            valor = randomicos[0]
            randomicos.remove(valor)
    agenda.append(Agenda.agendamentoChegada(None, agenda[indiceRetirada].getTempo(), randomicos[0], 0, 0))
    valor = randomicos[0]
    randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior
    
def saida(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    filas[0].subOcupante()
    if filas[0].getOcupantes() >= filas[0].getServidores():
        agenda.append(Agenda.agendamentoSaida(None, agenda[indiceRetirada].getTempo(), randomicos[0]))
        valor = randomicos[0]
        randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior

def proximo1(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    valor = randomicos[0]
    filas[0].subOcupante()
    if filas[0].getOcupantes() >= filas[0].getServidores():
        if randint(0,1) <= 0.8:
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 2))
            filas[1].addOcupante()
            if filas[1].getOcupantes() <= filas[1].getServidores():
                randomicos.remove(valor)
                filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior = proximo2(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior)
        else:
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 3))
            filas[2].addOcupante()
            if filas[2].getOcupantes() <= filas[2].getServidores():
                randomicos.remove(valor)
                filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior = proximo3(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior)

    return filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior
    
def proximo2(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior):
    valor = randomicos[0]
    filas[1].subOcupante()
    if filas[1].getOcupantes() >= filas[1].getServidores():
        rand = randint(0,1)
        if rand <= 0.5:
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
            filas[2].addOcupante()
            if filas[2].getOcupantes() <= filas[2].getServidores():
                randomicos.remove(valor)
                filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior = proximo3(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior)
        if rand > 0.5 and rand <= 0.8:
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
            filas[0].addOcupante()
            if filas[0].getOcupantes() <= filas[0].getServidores():
                randomicos.remove(valor)
                filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior = proximo1(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior)
        else:
            agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
            randomicos.remove(valor)
            filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior = saida(filas, agenda, indiceRetirada, randomicos, valor, tempoAnterior)
        
# Sorteia os números pseudo-aleatórios
def calcula(x0, a, c, m):
    randomicos=[]
    count = 0
    while(count < m):
        randomico=(a * x0 + c) % m
        randomico = randomico/m
        x0=randomico
        randomicos.append(randomico)
        count+=1
    return randomicos

def calculaMedia(calcula_media):
    count = 0
    result = []
    for _ in range(1):
            result.append(0)
    while count < 1:
        for index in range(len(calcula_media[count])):
            result[index] += calcula_media[count][index]
        count+=1
    for i in range(len(result)):
        result[i] = result[i] / 1
    print("Media das execucoes ===> ",result)


criaFilas()