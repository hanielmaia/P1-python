lista = []
contp = 0
contw = 0
contc = 0
for i in range(10):
    camisa = input('Qual a cor da camisa que voce vai querer?: ')
    contc += 1
    lista.append(camisa)
    if camisa == 'preta':
        contp += 1
    elif camisa == 'white':
        contw += 1
    



print(lista)
print('Total de camisas = ', contc)
print('Total de camisas brancas =', contw)
print('Total de camisas pretas =', contp)

