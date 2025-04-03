import random
def media(lista):
    media = sum(lista) / len(lista)


    return media

def qnt_acima_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if(lista[i] > media):
            qtd += 1
    return qtd

def qnt_abaixo_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if(lista[i] < media):
            qtd += 1
    return qtd

def qnt_igual_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if(lista[i] == media):
            qtd += 1
    return qtd

def elementos_acima_media(lista):
    acima_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if (lista[i] > media):
            acima_media.append(lista[i])
    return acima_media

def elementos_abaixo_media(lista):
    abaixo_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if (lista[i] < media):
            abaixo_media.append(lista[i])
    return abaixo_media

def elementos_igual_media(lista):
    igual_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if (lista[i] == media):
            iguaç_media.append(lista[i])
    return igual_media

def gerar_lista(tam):
    lista = []
    for i in range(tam):
        random.randint(0,100)
        lista.append(random.randint(0,100))

    return lista

    



#programa prncipal
l = gerar_lista(20)
print(l)
print(media(l))
print(qnt_acima_media(l))
print(qnt_abaixo_media(l))
print(qnt_igual_media(l))
print(elementos_acima_media(l))
print(elementos_abaixo_media(l))
print(elementos_igual_media(l))

