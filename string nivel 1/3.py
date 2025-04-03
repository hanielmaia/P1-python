word = input('aqui: ')
num = int(input('numero: '))

for i in range(len(word)):
    print(word[i], end=' ' * num)
