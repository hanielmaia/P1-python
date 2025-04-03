arq = open("sorteios.csv", "r")
registro = arq.read().splitlines()
arq.close


def obter_data(registro: list) -> list:

    data = registro[1]
    partes_data = data.split("/")  #
    dia = int(partes_data[0])
    mes = int(partes_data[1])
    ano = int(partes_data[2])
    return [dia, mes, ano]


def obter_ganhadores(registro: list, tipo: int) -> int:

    if tipo == 0:
        return int(registro[8])  # Sena
    elif tipo == 1:
        return int(registro[9])  # Quina
    elif tipo == 2:
        return int(registro[10])  # Quadra
    else:
        return 0


def quantidade_sorteios_por_ano(registros: list, ano: int) -> int:

    contador = 0
    for registro in registros:
        data = obter_data(registro)
        if data[2] == ano:
            contador += 1
    return contador


def quantidade_ganhadores_tipo(registros: list, tipo: int) -> int:

    total = 0
    for registro in registros:
        total += obter_ganhadores(registro, tipo)
    return total


registros = []
arquivo = open("sorteio.csv", "r")
linhas = arquivo.read().splitlines()
arquivo.close()

for i in range(1, len(linhas)):
    linha = linhas[i].split(";")
    registros.append(linha)


dicionario_sorteios_por_ano = {}
for ano in range(1996, 2026):
    dicionario_sorteios_por_ano[ano] = quantidade_sorteios_por_ano(registros, ano)

# Quantidade total de ganhadores
total_quadra = quantidade_ganhadores_tipo(registros, 2)
total_quina = quantidade_ganhadores_tipo(registros, 1)
total_sena = quantidade_ganhadores_tipo(registros, 0)


print("Quantidade total de sorteios por ano:")
for ano in dicionario_sorteios_por_ano:
    print(f"{ano}: {dicionario_sorteios_por_ano[ano]}")

print("\nQuantidade total de apostas ganhadoras:")
print(f"Quadra: {total_quadra}")
print(f"Quina: {total_quina}")
print(f"Sena: {total_sena}")


dicionario_sorteios_por_ano = {}
for ano in range(1996, 2026):
    dicionario_sorteios_por_ano[ano] = quantidade_sorteios_por_ano(registros, ano)


total_quadra = quantidade_ganhadores_tipo(registros, 2)
total_quina = quantidade_ganhadores_tipo(registros, 1)
total_sena = quantidade_ganhadores_tipo(registros, 0)


print("Quantidade total de sorteios por ano:")
for ano in dicionario_sorteios_por_ano:
    print(f"{ano}: {dicionario_sorteios_por_ano[ano]}")

print("\nQuantidade total de apostas ganhadoras:")
print(f"Quadra: {total_quadra}")
print(f"Quina: {total_quina}")
print(f"Sena: {total_sena}")
