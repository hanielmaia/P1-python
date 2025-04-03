maius = 0
minus = 0
num = 0


frase = input('frase: ')

for i in range(len(frase)):
    if frase[i].isupper() == True:
        maius += 1

    if frase[i].islower() == True:
        minus += 1

    if frase[i].isnumeric() == True:
        num += 1

print(maius)
print(minus)
print(num)