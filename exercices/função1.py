import random


def gerar_lista(tam):
    lista = []
    for i in range(tam):
        lista.append(random.randint(0, 100))
    return lista


def media(lista):
    media = sum(lista) / len(lista)
    return media


def qnt_acima_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] > media:
            qtd += 1
    return qtd


def qnt_abaixo_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] < media:
            qtd += 1
    return qtd


def qnt_igual_media(lista):
    qtd = 0
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] == media:
            qtd += 1
    return qtd


def elementos_acima_media(lista):
    acima_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] > media:
            acima_media.append(lista[i])
    return acima_media


def elementos_abaixo_media(lista):
    abaixo_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] < media:
            abaixo_media.append(lista[i])
    return abaixo_media


def elementos_igual_media(lista):
    igual_media = []
    media = sum(lista) / len(lista)
    for i in range(len(lista)):
        if lista[i] == media:
            igual_media.append(lista[i])
    return igual_media


# Rodar Programa
l = gerar_lista(20)
print("lista gerada", l)
print("media = ", media(l))
print("quantidade acima da media = ", qnt_acima_media(l))
print("quantidade abaixo da media = ", qnt_abaixo_media(l))
print("quantidade igual a media =", qnt_igual_media(l))
print("elementos acima da media =", elementos_acima_media(l))
print("elementos abaixo da media = ", elementos_abaixo_media(l))
print("elementos abaixo da media =", elementos_igual_media(l))
