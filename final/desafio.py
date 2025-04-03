matriz = []


for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f'digite os valores de [{i}] e [{j}]: '))
        linha.append(valor)
    matriz.append(linha)

print('matriz gerada: ')
for linha in matriz:
    print(linha)


soma_diagonal = 0

for i in range(len(matriz)):
    soma_diagonal += matriz[i][i]

print(soma_diagonal)