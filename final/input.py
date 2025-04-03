linhas = int(input('linhas: '))
colunas =int(input('linhas: '))

matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f'valor de [{i}][{j}]: '))
        linha.append(valor)
    matriz.append(linha)

print('matriz gerada')
for linha in matriz:
    print(linha)


soma_diagonal = 0

for i in range(len(matriz)):
    soma_diagonal += matriz[i][i]