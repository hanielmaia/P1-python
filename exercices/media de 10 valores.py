notas = int(input('Digite uma nota: '))
maior_nota = 0
soma = notas + notas + notas + notas + notas + notas + notas + notas + notas + notas
media = soma / 10

for i in range(1,10):
    notas = int(input('digite uma nota:'))

    if notas > maior_nota:
        maior_nota = notas
        

print(f'media = {media}')
print(f'a maior nota é {maior_nota}.') 