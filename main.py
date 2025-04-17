import random

from domanda import Domanda

file = open("domande.txt", "r").read().splitlines()
domande = []
for d in range(0, len(file), 7):
    domande.append(Domanda(testo=file[d], livello=file[d+1], corretta=file[d+2], opzioni=file[d+2:d+6]))

livelloCorrente = 0
punti = 0

# inizia il gioco

flag = True
while (flag):

    domandaCorrente = [x for x in domande if int(x.livello) == livelloCorrente]
    opzioni = domandaCorrente[0].opzioni

    print("livello = " + domandaCorrente[0].livello,"\ndomanda: " + domandaCorrente[0].testo ,"\nopzioni :" )

    for i in range(len(domandaCorrente[0].opzioniRandom())):
        print(str(domandaCorrente[0].opzioni[i]))

    risposta = input("inserisci risposta: ")
    if risposta == domandaCorrente[0].corretta:
        livelloCorrente += 1
        punti += 1
        print("risposta corretta, livello successivo:" + str(livelloCorrente))

    else:
        print("risposta errata" + ", punteggio: " + str(punti))
        flag = False





