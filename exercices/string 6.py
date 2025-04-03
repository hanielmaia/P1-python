senha = input("Digite a senha: ")

passouA = False
passouB = False
passouC = False
passouD = False
passouE = False

if len(senha) > 6:
    passouA = True

for letra in senha:
    if letra.islower():
        passouB = True

    if letra.isupper():
        passouC = True

    if letra.isdigit():
        passouD = True

    if not letra.isalnum():
        passouE = True

if passouA and passouB and passouC and passouD and passouE:
    print("Senha válida")
else:
    print("Senha inválida")
