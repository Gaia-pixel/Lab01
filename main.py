import random

from domanda import Domanda
from giocatori import Giocatori

file = open("domande.txt", "r").read().splitlines()
domande = []
for d in range(0, len(file), 7):
    domande.append(Domanda(testo=file[d], livello=file[d+1], corretta=file[d+2], opzioni=file[d+2:d+6]))

livelloCorrente = 0
max_liv = max(domande, key=lambda x: x.livello).livello
punti = 0

# inizia il gioco

flag = True
while (flag):

    domandeLiv = [x for x in domande if int(x.livello) == livelloCorrente]
    opzioni = domandeLiv[0].opzioni

    print("livello = " + domandeLiv[0].livello,"\ndomanda: " + domandeLiv[0].testo ,"\nopzioni :" )

    for i in range(len(domandeLiv[0].opzioniRandom())):
        print(str(domandeLiv[0].opzioni[i]))

    risposta = input("inserisci risposta: ")
    if risposta == domandeLiv[0].corretta:
        livelloCorrente += 1
        punti += 1
        print("risposta corretta, livello successivo: " + str(livelloCorrente))
        if livelloCorrente > int(max_liv):
            print("Hai vinto! Punteggio: ", punti)
            flag = False
            nick = input("Inserisci nickname: ")
    else:
        print("risposta errata" + ", punteggio: " + str(punti))
        flag = False
        nick = input("Inserisci nickname: ")


f = open("punti.txt", "r").read().splitlines()
g=[]
for i in range(len(f)):
    g.append(Giocatori(giocatore=f[i].split(' ')[0], punti=f[i].split(' ')[1]))
g.append(Giocatori(giocatore=nick, punti=punti))

g.sort(key=lambda x: int(x.punti), reverse=True)

with open('punti.txt', 'w') as f:
    for j in g:
        nick = j.giocatore
        punti = j.punti
        f.write(nick+ ' ' + str(punti) + '\n')


