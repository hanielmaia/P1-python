maior_nota = 0
soma = 0

qtd_notas = int(input('Digite a quantidade de notas: '))

for i in range(qtd_notas):
    nota = int(input('Digite uma nota: '))
    soma += nota

    if nota > maior_nota:
        maior_nota = nota

media = soma / qtd_notas

print(f'a maior nota é : {maior_nota}')
print(f'média = {media}')