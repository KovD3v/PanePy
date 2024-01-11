#include <iostream>
#include <vector>
#include <algorithm>

class Card {
public:
    std::string seed;
    int value;

    Card(std::string seed, int value) : seed(seed), value(value) {}

    friend std::ostream& operator<<(std::ostream& os, const Card& card) {
        os << card.value << " di " << card.seed;
        return os;
    }
};

class Player {
public:
    std::string nickname;
    std::vector<Card> deck;

    Player(std::string nickname, std::vector<Card> deck) : nickname(nickname), deck(deck) {}

    float evaluate() const {
        float points = 0;
        for (const Card& card : deck) {
            points += (card.value <= 7) ? card.value : 0.5;
        }
        return points;
    }
};

void shuffleDeck(std::vector<Card>& cards) {
    std::random_shuffle(cards.begin(), cards.end());
}

int main() {
    std::vector<Card> cards;
    std::vector<std::string> seeds = {"denara", "bastoni", "coppe", "spade"};
    std::vector<int> numbers(10);
    std::iota(numbers.begin(), numbers.end(), 1);  // Filling numbers from 1 to 10

    for (const std::string& seed : seeds) {
        for (int number : numbers) {
            cards.emplace_back(seed, number);
        }
    }

    shuffleDeck(cards);

    std::vector<Card> bank;
    Player player("", {});
    player.deck.push_back(cards.back());
    cards.pop_back();

    std::cout << "Hai pescato " << player.deck[0] << " (il tuo punteggio è " << player.evaluate() << ")\n";

    bank.push_back(cards.back());
    cards.pop_back();
    float bankPoint = 0;

    for (const Card& card : bank) {
        bankPoint += (card.value <= 7) ? card.value : 0.5;
    }

    std::cout << "La banca ha pescato " << bank[0] << " (il suo punteggio è " << bankPoint << ")\n";

    std::string choose = "y";
    bool playerOff = false;
    bool bankOff = false;

    while (true) {
        // loop fino a break
        bool valid = false;
        while (!valid) {
            // valida scelta solo y o n
            std::cout << "vuoi pescare un'altra carta? (y/n) ";
            std::cin >> choose;
            valid = (choose == "y") || (choose == "n");
        }
        if (choose == "y") {
            // se scelto si pesca e stampa
            Card cartaPescataPlayer = cards.back();
            cards.pop_back();
            player.deck.push_back(cartaPescataPlayer);
            std::cout << "hai pescato " << player.deck.back() << " che vale "
                      << ((cartaPescataPlayer.value <= 7) ? cartaPescataPlayer.value : 0.5)
                      << " il suo punteggio è ora (" << player.evaluate() << ")\n";
            if (player.evaluate() > 7.5) {
                playerOff = true;
                break;
            }
        } else {
            // se scelto no esci dal loop
            break;
        }
    }

    while ((player.evaluate() >= bankPoint) && (bankPoint <= 7.5) && !playerOff) {
        Card cartaPescata = cards.back();
        cards.pop_back();
        bank.push_back(cartaPescata);
        bankPoint += (cartaPescata.value <= 7) ? cartaPescata.value : 0.5;
        std::cout << "La banca ha pescato: " << cartaPescata << " che vale "
                  << ((cartaPescata.value <= 7) ? cartaPescata.value : 0.5) << " il suo punteggio è ora (" << bankPoint << ")\n";
        if (bankPoint > 7.5) {
            bankOff = true;
            break;
        }
    }

    if (playerOff && bankOff) {
        std::cout << "you lost, you have gone off first but the bank too\n";
    } else if (playerOff) {
        std::cout << "you lost, you have gone off\n";
    } else if (bankOff) {
        std::cout << "you win, bank has gone off\n";
    } else if (player.evaluate() <= bankPoint) {
        std::cout << "you lost\n";
    } else {
        std::cout << "you win\n";
    }

    return 0;
}
