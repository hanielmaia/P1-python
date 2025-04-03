frase = input('Digite uma frase: ')
frase_m = ""

for i in frase:
    if i in "0123456789":
        frase_m += "*"
    elif i.isupper():
        print (i)
    else:
    
        frase_m += i


print(frase_m)
