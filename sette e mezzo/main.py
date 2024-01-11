from random import shuffle

class Card:
    def __init__(self, seed, value):
        self.seed = seed
        self.value = value
    
    def __repr__(self):
        return(f"{self.value} di {self.seed}")

class Player:
    def __init__(self, nickname, deck: list[Card]):
        self.nickname = nickname
        self.deck = deck
        
    def evaluate(self):
        points = 0
        for card in self.deck:
            points += card.value if card.value <= 7 else 0.5
        return points
        

seeds = ['denara', "bastoni", "coppe", "spade"]
numbers = range(1,11)

cards = []

for seed in seeds:
    for number in numbers:
        cards.append(Card(seed, number))
        
shuffle(cards)

def main():
    bank: list[Card] = []
    player = Player(input('Inserisci il tuo nome: '), [])
    player.deck.append(cards.pop())
    print(f"Hai pescato {player.deck[0]} (il tuo punteggio è {player.evaluate()})")
    bank.append(cards.pop())
    bankPoint = 0
    for card in bank:
        bankPoint += card.value if card.value <= 7 else 0.5
    print(f"La banca ha pescato {bank[0]} (il suo punteggio è {bankPoint})")
    choose = "y"
    playerOff = False
    bankOff = False
    while True:
        # loop fino a break
        valid = False
        while not valid:
            # valida scelta solo y o n
            choose = input(f"vuoi pescare un'altra carta? (y/n) ")
            valid = choose == "y" or choose == "n"
        if choose == "y":
            # se scelto si pesca e stampa
            cartaPescataPlayer = cards.pop()
            player.deck.append(cartaPescataPlayer)
            print(f"hai pescato {player.deck[-1]} che vale {cartaPescataPlayer.value if cartaPescataPlayer.value <=7 else 0.5} il suo punteggio è ora ({player.evaluate()})")
            if player.evaluate() > 7.5:
                playerOff = True
                break
        else:
            # se scelto no esci dal loop
            break
    while player.evaluate() >= bankPoint <= 7.5 and not playerOff:
        cartaPescata = cards.pop()
        bank.append(cartaPescata)
        bankPoint += cartaPescata.value if cartaPescata.value <= 7 else 0.5
        print(f"La banca ha pescato: {cartaPescata} che vale {cartaPescata.value if cartaPescata.value <=7 else 0.5} il suo punteggio è ora ({bankPoint})")
        if bankPoint > 7.5:
            bankOff = True
            break
    
    if playerOff and bankOff:
        print("you lost, you have gone off first but the bank too")
    elif playerOff:
        print("you lost, you have gone off")
    elif bankOff:
        print("you win, bank has gone off")
    elif player.evaluate() <=bankPoint:
        print("you lost")
    else:
        print("you win")

main()