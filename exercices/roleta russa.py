import random

x = random.randint(0, 5)


for i in range(6):
    interacao = input('Deseja continuar? s / n: ')

    if i == x:
        if interacao == 's':
            print('infelizmente voce perdeu')
            print(f'o numero aleatório era {x}')
            break

        elif interacao == 'n':
            print('felizmente voce ganhou')
            print(f'o numero aleatório era {x}')
            break

