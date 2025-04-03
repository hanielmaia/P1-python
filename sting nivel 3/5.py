senha = input('digite sua senha: ')

passouA = False
passouB = False
passouC = False
passouD = False
passouE = False

if (len(senha)) > 6:
    passouA = True

for caractere in senha:
    if caractere.islower():
        passouB = True

for caractere in senha:
    if caractere.isupper():
        passouC = True

for caractere in senha:
    if caractere.isnumeric():
        passouD = True


for caractere in senha:
    if caractere.isalnum() == False:
        passouE = True


if passouA and passouB and passouC and passouD and passouE == True:
    print('senha válida')
else:
    print('senha invalida')
