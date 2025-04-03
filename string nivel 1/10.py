frase = input('frase: ')
vogais = 'aeiou'
cont = 0


for i in range(len(frase)):
    frase = frase.lower()

    if frase[i] in vogais:
        cont += 1
    
    

print(cont)

