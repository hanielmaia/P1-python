def misterio(lista):
    valor1 = lista[0]
    valor2 = None

    for i in range(len(lista)):
        if (lista[i] > valor1):
            valor2 = valor1
            valor1 = lista[i]
        else:
            if (lista[i] < valor1):
                if(valor2 is None or lista[i] > valor2):
                    valor2 = lista[i]
    return valor2

# O objetivo do código é descobrir o segundo maior número da lista e exibi-lo.

# Teste 1
lista = [1, 5, 3, 9, 8]
print(f"Resultado Teste 1: {misterio(lista)}")  # Esperado: 8

# Teste 2
lista = [-10, -20, -5, -30, -25]
print(f"Resultado Teste 2: {misterio(lista)}")  # Esperado: -10

# Teste 3
lista = [5, 5, 5, 5]
print(f"Resultado Teste 3: {misterio(lista)}")  # Esperado: None

# Teste 4
lista = [7]
print(f"Resultado Teste 4: {misterio(lista)}")  # Esperado: None

# Teste 5
lista = [12, 8]
print(f"Resultado Teste 5: {misterio(lista)}")  # Esperado: 8
