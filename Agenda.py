class Agenda:

    def __init__(self, evento, tempo, sorteio, prevFila, novaFila):
        self.evento = evento
        self.tempo = tempo
        self.sorteio = sorteio
        self.prevFila = prevFila
        self.novaFila = novaFila

    def agendamentoChegada(self, tempo, sorteio, prevFila, novaFila):
        sort = (4 - 1) * sorteio + 1
        return Agenda("chegada", tempo + sort, sort, prevFila, novaFila)

    def agendamentoSaida2(self, tempo, sorteio, prevFila, novaFila):
        sort = (10 - 5) * sorteio + 5
        return Agenda("saida2", tempo + sort, sort, prevFila, novaFila)

    def agendamentoSaida3(self, tempo, sorteio, prevFila, novaFila):
        sort = (20 - 10) * sorteio + 10
        return Agenda("saida3", tempo + sort, sort, prevFila, novaFila)

    def agendamentoProximo1(self, tempo, sorteio, prevFila, novaFila):
        sort = (1.5 - 1) * sorteio + 1
        return Agenda("proximo1", tempo + sort, sort, prevFila, novaFila)

    def agendamentoProximo2(self, tempo, sorteio, prevFila, novaFila):
        sort = (10 - 5) * sorteio + 5
        return Agenda("proximo2", tempo + sort, sort, prevFila, novaFila)

    def agendamentoProximo3(self, tempo, sorteio, prevFila, novaFila):
        sort = (20 - 10) * sorteio + 10
        return Agenda("proximo3", tempo + sort, sort, prevFila, novaFila)

    def getEvento(self):
        return str(self.evento)

    def getTempo(self):
        return self.tempo

    def getSorteio(self):
        return self.sorteio

    def getPrevFila(self):
        return self.prevFila

    def getNovaFila2(self):
        return self.novoFila