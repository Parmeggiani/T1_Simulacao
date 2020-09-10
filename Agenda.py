class Agenda:

    def __init__(self, evento, tempo, sorteio):
        self.evento = evento
        self.tempo = tempo
        self.sorteio = sorteio

    def agendamentoChegada(self, tempo, sorteio):
        sort = (4 - 2) * sorteio + 2
        return Agenda("chegada", tempo + sort, sort)

    def agendamentoSaida(self, tempo, sorteio):
        sort = (5 - 3) * sorteio + 3
        return Agenda("saida", tempo + sort, sort)

    def getEvento(self):
        return str(self.evento)

    def getTempo(self):
        return self.tempo

    def getSorteio(self):
        return self.sorteio
