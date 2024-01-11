from random import randint

print("Welcome to Rock, Paper, Scissors!")
print("1) Rock")
print("2) Paper")
print("3) Scissors")
y = int(input("Enter a number: "))
x = randint(1, 3)

match x:
    case 1:
        print("The computer choose Rock")
    case 2:
        print("The computer choose Paper")
    case 3:
        print("The computer choose Scissors")

if x == y:
    print("Draw")
elif x == 1 and y == 3:
    print("You lose")
elif x == 3 and y == 1:
    print("You win")
elif x < y:
    print("You win")
else:
    print("You lose")