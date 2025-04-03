frase = input('frase: ')
nova_frase = ''

for i in range(len(frase)):
    if frase[i].isdigit() == True:
        nova_frase += '*'

    else:
        nova_frase += frase[i]

print('Não houve alterações, frase = ', frase)
print('nova frase = ', nova_frase)