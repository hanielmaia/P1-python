n1 = float(input('Qual a nota da sua primeira prova?: '))
n2 = float(input('Qual a nota da sua segunda prova?: '))
n3 = float(input('Qual a nota da sua terceira prova?: '))
soma = n1 + n2 + n3
nf = soma / 3
media = 70
qp = media - nf

if nf >= media:
    print(f'Parabéns, sua média final ficou {nf}, voce está aprovado por média! Boas Férias!')

else:
    print(f'Voce precisa de {qp} pontos para ser aprovado por Média, Veja os calendários das recuperações. Sua Média:{nf} ')
    print('Digite (sim) se quiser olhar o calendario das recuperações,caso nao queria, so digitar (não)')
    sim = str(input('Deseja olhar o calendario das recuperações?: '))
    if sim:
      print('Clique no link a seguir para acompanhar as datas das avaliações de recuperações: D:/estudos/html-css/exercicios/ex009/index.html')

else:
          print('ola')
  
    
   
        

