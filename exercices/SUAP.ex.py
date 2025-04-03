nota = int(input())
qtd = 0

while (nota < 0 or nota > 100):
    nota = int(input())

    if nota != (nota <= 0 or nota > 100):
        qtd += 1

    elif nota > 0 or nota <=  100:
        break

 
print(f'{nota} {qtd}')
