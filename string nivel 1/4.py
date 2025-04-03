frase = input('frase: ')
cont = 0
for i in range(len(frase)):
    if frase[i] == 'F':
        cont += 1

print(frase)
print(cont)
