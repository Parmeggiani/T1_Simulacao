import Filas
import Agenda
import Math

tempo_global = 0


def main():
    fila1 = Filas(0, 200)
    fila2 = Filas(0, 100)
    fila3 = Filas(0, 1000)

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
            fila1.atualizaTempo(fila1.getOcupantes(), index.getTempo() - tempoAnterior))
            tempoAnterior=index.getTempo()
            if fila1.getOcupantes < 200:
                fila1.addOcupante()
                if fila1.getOcupantes() <= 1:
                    agenda.append(Agenda.agendamentoSaida(
                        index.getTempo(), resultado[0]))
                    resultado.remove(0)
            agenda.append(Agenda.agendamentoChegada(
                index.getTempo(), resultado[0]))
            resultado.remove(0)

        if agenda[indiceRetirada].getEvento() == "saida":
            fila1.atualizaTempo(fila1.getOcupantes(), index.getTempo() - tempoAnterior))
            tempoAnterior=index.getTempo()
            fila1.subOcupante()
            if fila1.getOcupantes() >= 1
                agenda.append(Agenda.agendamentoSaida(
                    index.getTempo(), resultado[0]))
                resultado.remove(0)
        resultado.remove(indiceRetirada)

# Sorteia os números pseudo-aleatórios


def calcula(x0, a, m, c):
    resultados=[]
    for index in range(m):
        resultado=(a * x0 + c) % m
        x0=resultado
        resultados.append(resultado)
    return resultados
