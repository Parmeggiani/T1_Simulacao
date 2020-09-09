import Filas
import Agenda
import Math

tempo_global = 0


def main():
    fila1 = Filas(200)
    fila2 = Filas(100)
    fila3 = Filas(1000)
    agenda = []

    resultado = calcula(120, 7, 1000, 5)
    agenda.append(Agenda("chegada", 10, 0))

    while(len(resultado) > 0):
        menorTempo = Math.inf()
        indiceRetirada = 0
        for index in agenda:
            if menorTempo > index.getTempo:
                menorTempo = index.getTempo
                indiceRetirada = index
        if agenda[indiceRetirada].getEvento() == "chegada":
            agenda.append(Agenda.agendamentoChegada(
                index.getTempo, resultado[0]))
            resultado.remove(0)
        resultado.remove(indiceRetirada)

# Sorteia os números pseudo-aleatórios


def calcula(x0, a, m, c):
    resultados = []
    for index in range(m):
        resultado = (a * x0 + c) % m
        x0 = resultado
        resultados.append(resultado)
    return resultados
