from random import randint

utente = int(input("choose a number from 0 to 5: "))
engine = randint(0, 5)

if engine == utente:
    print('Correct')
else:
    print('Wrong')

print("He choose " + str(engine))
