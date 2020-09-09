import Filas
import Agenda

tempo_global = 0

def main():
    fila1 = Filas(200)
    fila2 = Filas(100)
    fila3 = Filas(1000)

    resultado = calcula( 120, 7, 1000, 5)

    Agenda('chegada', 10, 0)

    fila1.chegada()


def calcula(x0, a, m, c):

    resultados = []
    for index in range(m):
        resultado = (a * x0 + c) % m
        x0 = resultado
        resultados..append(resultado)
    return resultados
