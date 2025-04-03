frase = input('Digite uma frase: ')
vogais = "aeiouAEIOU"
cont = 0
for i in frase:
    if i in vogais:
        cont += 1

print('Quantidade de vogais', cont)