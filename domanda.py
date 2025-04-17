import random


class Domanda():
    def __init__(self, testo="", livello=None, corretta="", opzioni=[]):
        self.testo=testo
        self.livello=livello
        self.corretta=corretta
        self.opzioni=opzioni

    def opzioniRandom(self):
        random.shuffle(self.opzioni)
        return self.opzioni

