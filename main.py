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
    #randomicos =  [0.2176,0.0103,0.1109,0.3456,0.9910,0.2323,0.9211,0.0322,0.1211,0.5131,0.7208,0.9172,0.9922,0.8324,0.5011,0.2931]
    main(randomicos,filas)
    #media_resultados.append(filas[0].getLista())
    #calculaMedia(media_resultados)
    

def main(randomicos,filas):

    tempoAnterior = 0
    agenda = []
    agenda.append(Agenda("chegada", 1, 0, 0, 0))

    while(len(randomicos) > 0):
        menorTempo = math.inf
        indiceRetirada = 0
        for index in range(len(agenda)):
            if menorTempo > agenda[index].getTempo():
                menorTempo = agenda[index].getTempo()
                indiceRetirada = index
        
        valor = randomicos[0]

        if agenda[indiceRetirada].getEvento() == "chegada":
            filas, agenda, indiceRetirada, randomicos, tempoAnterior = chegada(filas, agenda, indiceRetirada, randomicos, tempoAnterior)

        elif agenda[indiceRetirada].getEvento() == "saida2":
            filas, agenda, indiceRetirada, randomicos, tempoAnterior = saida2(filas, agenda, indiceRetirada, randomicos, tempoAnterior)
        
        elif agenda[indiceRetirada].getEvento() == "saida3":
            filas, agenda, indiceRetirada, randomicos, tempoAnterior = saida3(filas, agenda, indiceRetirada, randomicos, tempoAnterior)

        elif agenda[indiceRetirada].getEvento() == "proximo1":
            filas, agenda, indiceRetirada, randomicos, tempoAnterior = proximo1(filas, agenda, indiceRetirada, randomicos, tempoAnterior)
        
        elif agenda[indiceRetirada].getEvento() == "proximo2":
            filas, agenda, indiceRetirada, randomicos, tempoAnterior = proximo2(filas, agenda, indiceRetirada, randomicos, tempoAnterior)
        
        elif agenda[indiceRetirada].getEvento() == "proximo3":
            filas, agenda, indiceRetirada, randomicos, tempoAnterior = proximo3(filas, agenda, indiceRetirada, randomicos, tempoAnterior)

        remove_da_agenda = agenda[indiceRetirada]
        agenda.remove(remove_da_agenda)
    print("Tempo",tempoAnterior)
    filas[0].printLista()
    filas[1].printLista()
    filas[2].printLista()


def chegada(filas, agenda, indiceRetirada, randomicos, tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    filas[0].addOcupante()
    if filas[0].getOcupantes() <= filas[0].getServidores():
        valor = randomicos[0]
        if valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 2))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    if(len(randomicos)==0):
        return filas, agenda, indiceRetirada, randomicos, tempoAnterior
    agenda.append(Agenda.agendamentoChegada(None, agenda[indiceRetirada].getTempo(), randomicos[0], 1, 1))
    valor = randomicos[0]
    randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
    
def saida2(filas, agenda, indiceRetirada, randomicos, tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    if(filas[1].getOcupantes()>0):
        filas[1].subOcupante()
    if filas[1].getOcupantes() >= filas[1].getServidores():
        valor = randomicos[0]
        if valor <= 0.5:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
        if valor > 0.5 and valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
        valor = randomicos[0]
        randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, tempoAnterior

def saida3(filas, agenda, indiceRetirada, randomicos,  tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    if(filas[2].getOcupantes()>0):
        filas[2].subOcupante()
    if filas[2].getOcupantes() >= filas[2].getServidores():
        valor = randomicos[0]
        if valor <= 0.7:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 2))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoSaida3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, tempoAnterior

def proximo1(filas, agenda, indiceRetirada, randomicos, tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    if(filas[0].getOcupantes()>0):
        filas[0].subOcupante()
    if filas[0].getOcupantes() >= filas[0].getServidores():
        valor = randomicos[0]
        if valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 2))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    indexFila = agenda[indiceRetirada].getNovaFila()-1
    if(filas[indexFila].getOcupantes() < filas[indexFila].getCapacidade()):
        filas[indexFila].addOcupante()
    if(len(randomicos)==0):
        return filas, agenda, indiceRetirada, randomicos, tempoAnterior
    if(filas[indexFila].getOcupantes() <= filas[indexFila].getServidores()):
        if(indexFila+1 == 2):
            valor = randomicos[0]
            if valor <= 0.5:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
            elif valor > 0.5 and valor <= 0.8:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
            else:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
        else:
            valor = randomicos[0]
            if valor <= 0.7:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoProximo3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 2))
            else:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoSaida3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
    
def proximo2(filas, agenda, indiceRetirada, randomicos, tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    if(filas[1].getOcupantes()>0):
        filas[1].subOcupante()
    if filas[1].getOcupantes() >= filas[1].getServidores():
        valor = randomicos[0]
        if valor <= 0.5:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
        elif valor > 0.5 and valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
        valor = randomicos[0]
        randomicos.remove(valor)
    indexFila = agenda[indiceRetirada].getNovaFila()-1
    if(filas[indexFila].getOcupantes() < filas[indexFila].getCapacidade()):
        filas[indexFila].addOcupante()
    if(len(randomicos)==0):
        return filas, agenda, indiceRetirada, randomicos, tempoAnterior
    if(filas[indexFila].getOcupantes() <= filas[indexFila].getServidores()):
        if(indexFila+1 == 1):
            valor = randomicos[0]
            if valor <= 0.8:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 2))
            else:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 3))
        else:
            if valor <= 0.7:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoProximo3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 2))
            else:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoAnterior
                agenda.append(Agenda.agendamentoSaida3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, tempoAnterior

def proximo3(filas, agenda, indiceRetirada, randomicos, tempoAnterior):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoAnterior)
    tempoAnterior = agenda[indiceRetirada].getTempo()
    if(filas[2].getOcupantes()>0):
        filas[2].subOcupante()
    if filas[2].getOcupantes() >= filas[2].getServidores():
        valor = randomicos[0]
        if valor <= 0.7:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos,  tempoAnterior
            agenda.append(Agenda.agendamentoProximo3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 2))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos,  tempoAnterior
            agenda.append(Agenda.agendamentoSaida3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    indexFila = agenda[indiceRetirada].getNovaFila()-1
    if(filas[indexFila].getOcupantes() < filas[indexFila].getCapacidade()):
        filas[indexFila].addOcupante()
    if(len(randomicos)==0):
        return filas, agenda, indiceRetirada, randomicos,  tempoAnterior
    if(filas[indexFila].getOcupantes() <= filas[indexFila].getServidores()):
        valor = randomicos[0]
        if valor <= 0.5:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoAnterior
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
        if valor > 0.5 and valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos,  tempoAnterior
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos,  tempoAnterior
            agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
        valor = randomicos[0]
        randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos,  tempoAnterior
    

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