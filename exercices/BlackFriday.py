honesto = 0
desonesto = 0 
##lembrar de trocar a quantidade de repetição no for 
for i in range(1,11):
    valor, valor_depois = input().split()
    valor, valor_depois = float(valor), float(valor_depois)

    if valor <= valor_depois:
        desonesto += 1

    elif valor >= valor_depois:
        honesto += 1
    
media_h = honesto * 10
media_d = desonesto * 10

print(f'honestos: {honesto} ({media_h:.1f}%)')
print(f'desonestos: {desonesto} ({media_d:.1f}%)')