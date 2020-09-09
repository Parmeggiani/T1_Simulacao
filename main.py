import Filas
import Agenda
import Math
import random

numero_filas = 0

filas = []

def criaFilas():
    f = read("config.txt", "r")
    numero_filas = f.readline()
    for index in range(numero_filas):
        aux = f.readline()
        aux = aux.split(" ")
        filas.append(Filas(int(aux[0]),int(aux[1])))


def main():
    tempoAnterior = 0

    agenda = []

    resultado = calcula(120, 7, 1000, 5)

    agenda.append(Agenda("chegada", 10, 0))

    while(len(resultado) > 0):
        menorTempo = Math.inf()
        indiceRetirada = 0
        for index in agenda:
            if menorTempo > index.getTempo():
                menorTempo = index.getTempo()
                indiceRetirada = index

        if agenda[indiceRetirada].getEvento() == "chegada":
            aux_fila = filas[selecionaFila(numero_filas)]
            aux_fila.atualizaTempo(aux_fila.getOcupantes(), index.getTempo() - tempoAnterior))
            tempoAnterior=index.getTempo()
            if aux_fila.getOcupantes < aux_fila.getCapacidade():
                aux_fila.addOcupante()
                if aux_fila.getOcupantes() <= 1:
                    agenda.append(Agenda.agendamentoSaida(index.getTempo(), resultado[0]))
                    resultado.remove(0)
            agenda.append(Agenda.agendamentoChegada(index.getTempo(), resultado[0]))
            resultado.remove(0)

        if agenda[indiceRetirada].getEvento() == "saida":
            aux_fila = filas[selecionaFila(numero_filas)]
            aux_fila.atualizaTempo(aux_fila.getOcupantes(), index.getTempo() - tempoAnterior))
            tempoAnterior=index.getTempo()
            aux_fila.subOcupante()
            if aux_fila.getOcupantes() >= 1
                agenda.append(Agenda.agendamentoSaida(index.getTempo(), resultado[0]))
                resultado.remove(0)
        resultado.remove(indiceRetirada)

def selecionaFila(numero_filas):
    return random.randint(0,numero_filas-1)

def roteamento():


# Sorteia os números pseudo-aleatórios

def calcula(x0, a, m, c):
    resultados=[]
    for index in range(m):
        resultado=(a * x0 + c) % m
        x0=resultado
        resultados.append(resultado)
    return resultados
