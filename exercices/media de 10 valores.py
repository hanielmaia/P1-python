
lista = []
notas = int(input('digite uma nota: '))
maior_nota = 0

for i in range(9):
    notas = int(input('digite uma nota: '))
    lista.append(notas)

soma = sum(lista)
media = soma / 10

print(f'Média = {media}')
