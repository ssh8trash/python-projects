import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'chuta um número de um a {x}: '))
        if guess < random_number:
            print("pra cima")
        elif guess > random_number:
          print("pra baixo")

    print(f"aqui é vasco nessa porra")

guess(100)
