maior = -1
contador = 0
media = 0
n = int(input('Digite o seu multiplicador: '))
    
for i in range(n):

    nota = int(input('Digite a sua nota: '))
    while (nota < 0) or (nota > 100):
        print('Nota invalida') 
        nota = int(input('Digite a sua nota: '))

    if (0 <= nota <= 100):
    
        contador += nota

    if (nota > maior): 
         maior = nota

media = contador/n

print(f'Média = {media:.2f}')
print('Maior = ',maior)