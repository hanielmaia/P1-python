while True:
    n = int(input('Digite o seu multiplicador: '))
    if (n < 4 or n > 10):
        print('Fora do intervalo')
        break

    maior = -1
    contador = 0
    soma = 0



    
    for i in range(n):
        nota = int(input('Digite a sua nota: '))

        while (nota < 0 or nota > 100):
              print('Nota invalida') 
              nota = int(input('Digite a sua nota: '))

        if (nota > maior): 
             maior = nota

        soma  += nota

    media = soma/n

    print(f'Média = {media:.2f}')
    print('Maior = ',maior)