senha = int(input())


while senha != 2002:
    print('Senha Invalida')
    senha = int(input())

    if senha == 2002:
        print('Acesso Permitido')
        break
    
