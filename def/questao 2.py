def comparar_data(dia:int, mes:int, ano:int) -> int:
    dia_atual, mes_atual, ano_atual = 13, 3, 2025

    if dia == dia_atual and mes == mes_atual and ano == ano_atual:
        return 0
    
    elif dia < dia_atual and mes <= mes_atual and ano <= ano_atual:
        return -1
    
    elif dia > dia_atual and mes >= mes_atual and ano >= ano_atual:
        return 1
    
    
def calcular_idade(dia:int, mes:int, ano:int) -> int:
    dia_atual, mes_atual, ano_atual = 13, 3, 2025
    if comparar_data(dia, mes, ano) == 0:
        idade = ano_atual - ano

    elif comparar_data(dia, mes, ano) == -1:
        idade = ano_atual - ano

    elif comparar_data(dia, mes, ano) == 1:
        idade = (ano_atual - ano) - 1

    return idade




soma = 0

for i in range(40):
    dia = input('')
    mes = input('')
    ano = input('')
    idade = calcular_idade(dia, mes, ano)
    soma += idade

media = soma / 40

print(media)



