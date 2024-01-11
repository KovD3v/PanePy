from random import randint

print("Welcome to Rock, Paper, Scissors!")
print("1) Rock")
print("2) Paper")
print("3) Scissors")
utente = int(input("Enter a number: "))
engine = randint(1, 3)

match engine:
    case 1:
        print("The computer choose Rock")
    case 2:
        print("The computer choose Paper")
    case 3:
        print("The computer choose Scissors")

if engine == utente:
    print("Draw")
elif engine == 1 and utente == 3:
    print("utente lose")
elif engine == 3 and utente == 1:
    print("utente win")
elif engine < utente:
    print("utente win")
else:
    print("utente lose")