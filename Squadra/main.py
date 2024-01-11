class Calciatore:
    def __init__(self, altezza):
        self.altezza = altezza
        
class Squadra:
    def __init__(self, nome, calciatori):
        self.nome = nome
        self.calciatori = calciatori
        
    def stampaMaggiore(self, altezzaMinima):
        for calciatore in self.calciatori:
            if calciatore.altezza >= altezzaMinima:
                print(str(calciatore.altezza) + " della squadra " + self.nome)

n = 2
m = 2
squadre = []
for i in range(n):
    nomeSquadra = input("Inserisci il nome della squadra: ")
    calciatori = []
    for j in range(m):
        altezza = int(input("Inserisci l'altezza del calciatore: "))
        calciatore = Calciatore(altezza)
        calciatori.append(calciatore)
    squadra = Squadra(nomeSquadra, calciatori)
    squadre.append(squadra)

altezzaMinima = 5

for squadra in squadre:
    squadra.stampaMaggiore(altezzaMinima)