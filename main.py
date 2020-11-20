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
    filas=[]
    while count < numero_filas:
        aux = f.readline()
        aux = aux.split(" ")
        filas.append(Filas(int(aux[0]), int(aux[1])))
        count+=1
    cal = f.readline()
    cal = cal.split(" ")
    randomicos = calcula(int(cal[0]), int(cal[1]), int(cal[2]), int(cal[3]))
    #randomicos =  [0.2176,0.0103,0.1109,0.3456,0.9910,0.2323,0.9211,0.0322,0.1211,0.5131,0.7208,0.9172,0.9922,0.8324,0.5011,0.2931]
    main(randomicos,filas)
    

def main(randomicos,filas):

    tempoGlobal = 0
    perdaFila1 = 0
    perdaFila2 = 0
    perdaFila3 = 0
    agenda = []
    agenda.append(Agenda("chegada", 1, 0, 0, 0))

    while(len(randomicos) > 0):
        menorTempo = math.inf
        indiceRetirada = 0
        for index in range(len(agenda)):
            if menorTempo > agenda[index].getTempo():
                menorTempo = agenda[index].getTempo()
                indiceRetirada = index

        if agenda[indiceRetirada].getEvento() == "chegada":
            filas, agenda, indiceRetirada, randomicos, tempoGlobal = chegada(filas, agenda, indiceRetirada, randomicos, tempoGlobal)

        elif agenda[indiceRetirada].getEvento() == "saida2":
            filas, agenda, indiceRetirada, randomicos, tempoGlobal = saida2(filas, agenda, indiceRetirada, randomicos, tempoGlobal)
        
        elif agenda[indiceRetirada].getEvento() == "saida3":
            filas, agenda, indiceRetirada, randomicos, tempoGlobal = saida3(filas, agenda, indiceRetirada, randomicos, tempoGlobal)

        elif agenda[indiceRetirada].getEvento() == "proximo1":
            filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3 = proximo1(filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3)
        
        elif agenda[indiceRetirada].getEvento() == "proximo2":
            filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3 = proximo2(filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3)
        
        elif agenda[indiceRetirada].getEvento() == "proximo3":
            filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2 = proximo3(filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2)

        remove_da_agenda = agenda[indiceRetirada]
        agenda.remove(remove_da_agenda)
    print("FILA 1")
    TempoEProbabilidade(filas, 0)
    print("Perda de clientes Fila 1 ==> ", perdaFila1)
    print("")
    print("FILA 2")
    TempoEProbabilidade(filas, 1)
    print("Perda de clientes Fila 2 ==> ", perdaFila2)
    print("")
    print("FILA 3")
    TempoEProbabilidade(filas, 2)
    print("Perda de clientes Fila 3 ==> ", perdaFila3)
    print("")
    print("Tempo Total ==> ",tempoGlobal)


def chegada(filas, agenda, indiceRetirada, randomicos, tempoGlobal):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    tempoGlobal = agenda[indiceRetirada].getTempo()
    filas[0].addOcupante()
    if filas[0].getOcupantes() <= filas[0].getServidores():
        valor = randomicos[0]
        if valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 2))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    if(len(randomicos)==0):
        return filas, agenda, indiceRetirada, randomicos, tempoGlobal
    agenda.append(Agenda.agendamentoChegada(None, agenda[indiceRetirada].getTempo(), randomicos[0], 1, 1))
    valor = randomicos[0]
    randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, tempoGlobal
    
def saida2(filas, agenda, indiceRetirada, randomicos, tempoGlobal):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    tempoGlobal = agenda[indiceRetirada].getTempo()
    if(filas[1].getOcupantes()>0):
        filas[1].subOcupante()
    if filas[1].getOcupantes() >= filas[1].getServidores():
        valor = randomicos[0]
        if valor <= 0.5:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
        elif valor > 0.5 and valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal
            agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
        valor = randomicos[0]
        randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, tempoGlobal

def saida3(filas, agenda, indiceRetirada, randomicos,  tempoGlobal):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    tempoGlobal = agenda[indiceRetirada].getTempo()
    if(filas[2].getOcupantes()>0):
        filas[2].subOcupante()
    if filas[2].getOcupantes() >= filas[2].getServidores():
        valor = randomicos[0]
        if valor <= 0.7:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal
            agenda.append(Agenda.agendamentoProximo3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 2))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal
            agenda.append(Agenda.agendamentoSaida3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    return filas, agenda, indiceRetirada, randomicos, tempoGlobal

def proximo1(filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    tempoGlobal = agenda[indiceRetirada].getTempo()
    if(filas[0].getOcupantes()>0):
        filas[0].subOcupante()
    if filas[0].getOcupantes() >= filas[0].getServidores():
        valor = randomicos[0]
        if valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 2))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
            agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    indexFila = agenda[indiceRetirada].getNovaFila()-1
    if(filas[indexFila].getOcupantes() < filas[indexFila].getCapacidade()):
        filas[indexFila].addOcupante()
        if(len(randomicos)==0):
            return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
        if(filas[indexFila].getOcupantes() <= filas[indexFila].getServidores()):
            if(indexFila+1 == 2):
                valor = randomicos[0]
                if valor <= 0.5:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
                    agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
                elif valor > 0.5 and valor <= 0.8:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
                    agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
                else:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
                    agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
            else:
                valor = randomicos[0]
                if valor <= 0.7:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
                    agenda.append(Agenda.agendamentoProximo3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 2))
                else:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
                    agenda.append(Agenda.agendamentoSaida3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 3))
            valor = randomicos[0]
            randomicos.remove(valor)
    else:
        if(indexFila+1 == 2):
            perdaFila2 = perdaFila2+1
        else:
            perdaFila3 = perdaFila3+1
    return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2,perdaFila3
    
def proximo2(filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    tempoGlobal = agenda[indiceRetirada].getTempo()
    if(filas[1].getOcupantes()>0):
        filas[1].subOcupante()
    if filas[1].getOcupantes() >= filas[1].getServidores():
        valor = randomicos[0]
        if valor <= 0.5:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
        elif valor > 0.5 and valor <= 0.8:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3
            agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3
            agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
        valor = randomicos[0]
        randomicos.remove(valor)
    indexFila = agenda[indiceRetirada].getNovaFila()-1
    if(filas[indexFila].getOcupantes() < filas[indexFila].getCapacidade()):
        filas[indexFila].addOcupante()
        if(len(randomicos)==0):
            return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3
        if(filas[indexFila].getOcupantes() <= filas[indexFila].getServidores()):
            if(indexFila+1 == 1):
                valor = randomicos[0]
                if valor <= 0.8:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3
                    agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 2))
                else:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3
                    agenda.append(Agenda.agendamentoProximo1(None,agenda[indiceRetirada].getTempo(), randomicos[0], 1, 3))
            else:
                valor = randomicos[0]
                if valor <= 0.7:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3
                    agenda.append(Agenda.agendamentoProximo3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 2))
                else:
                    randomicos.remove(valor)
                    if(len(randomicos)==0):
                        return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3
                    agenda.append(Agenda.agendamentoSaida3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 3))
            valor = randomicos[0]
            randomicos.remove(valor)
    else:
        perdaFila3 = perdaFila3+1
    return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila3

def proximo3(filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2):
    filas[0].atualizaTempo(filas[0].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[1].atualizaTempo(filas[1].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    filas[2].atualizaTempo(filas[2].getOcupantes(), agenda[indiceRetirada].getTempo() - tempoGlobal)
    tempoGlobal = agenda[indiceRetirada].getTempo()
    if(filas[2].getOcupantes()>0):
        filas[2].subOcupante()
    if filas[2].getOcupantes() >= filas[2].getServidores():
        valor = randomicos[0]
        if valor <= 0.7:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2
            agenda.append(Agenda.agendamentoProximo3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 2))
        else:
            randomicos.remove(valor)
            if(len(randomicos)==0):
                return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2
            agenda.append(Agenda.agendamentoSaida3(None,agenda[indiceRetirada].getTempo(), randomicos[0], 3, 3))
        valor = randomicos[0]
        randomicos.remove(valor)
    indexFila = agenda[indiceRetirada].getNovaFila()-1
    if(filas[indexFila].getOcupantes() < filas[indexFila].getCapacidade()):
        filas[indexFila].addOcupante()
        if(len(randomicos)==0):
            return filas, agenda, indiceRetirada, randomicos,  tempoGlobal, perdaFila2
        if(filas[indexFila].getOcupantes() <= filas[indexFila].getServidores()):
            valor = randomicos[0]
            if valor <= 0.5:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos, tempoGlobal, perdaFila2
                agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 3))
            elif valor > 0.5 and valor <= 0.8:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos,  tempoGlobal, perdaFila2
                agenda.append(Agenda.agendamentoProximo2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 1))
            else:
                randomicos.remove(valor)
                if(len(randomicos)==0):
                    return filas, agenda, indiceRetirada, randomicos,  tempoGlobal, perdaFila2
                agenda.append(Agenda.agendamentoSaida2(None,agenda[indiceRetirada].getTempo(), randomicos[0], 2, 2))
            valor = randomicos[0]
            randomicos.remove(valor)
    else:
        perdaFila2 = perdaFila2+1
    return filas, agenda, indiceRetirada, randomicos,  tempoGlobal, perdaFila2
    

# Sorteia os números pseudo-aleatórios
def calcula(x0, a, c, m):
    randomicos=[]
    count = 0
    while(count < 100000):
        randomico=(a * x0 + c) % m
        x0=randomico
        randomico = randomico/m
        randomicos.append(randomico)
        count+=1
    return randomicos

def TempoEProbabilidade(filas, numFila):
    prob = []
    cont=0
    fila=filas[numFila].getLista()
    totalprob = 0
    while(cont < len(fila)):
        if fila[cont] == 0:
            break
        totalprob+= fila[cont]
        cont+=1
    cont=0
    while(cont < len(fila)):
        if fila[cont] == 0:
            break
        prob.append((fila[cont]*100)/totalprob)
        cont+=1
    cont=0
    while(cont < len(prob)):
        print(cont," ==> Tempos", fila[cont],"==> Probabilidade ",prob[cont],"%")
        cont+=1

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