class Agenda:

    def __init__(self, evento, tempo, sorteio):
        self.evento = evento
        self.tempo = tempo
        self.sorteio = sorteio

    def agendamentoChegada(self, tempo, sorteio):
        sort = (4 - 1) * sorteio + 1
        return Agenda("chegada", tempo + sort, sort)

    def agendamentoSaida(self, tempo, sorteio):
        sort = (10 - 5) * sorteio + 5
        return Agenda("saida", tempo + sort, sort)

    def getEvento(self):
        return self.evento

    def getTempo(self):
        return self.tempo

    def getSorteio(self):
        return self.sorteio
