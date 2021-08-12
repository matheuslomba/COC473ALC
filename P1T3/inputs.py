from sup import finaliza

#-----------------------------------------------------------------------------

def pontox():
    print('=' * 30)
    while True:
        try:
            x = float(input('O programa deverá calcular o y de qual ponto x? '))
            break
        except ValueError:
                print('Favor inserir um número (float).')
    return x

#-----------------------------------------------------------------------------

def coordenadas(paresN):

    listapontos = [[]]
    print('=' * 30)

    for i in range(0, paresN):
        for j in range(0, 2):
            try:
                if j == 0:
                    listapontos[i].append(float(input(f'{i + 1}º Coordenada: x = ')))
                else:
                    listapontos[i].append(float(input(f'{i + 1}º Coordenada: y = ')))
            except ValueError:
                print("Favor rodar o programa novamente e inserir um número válido (float).")
                finaliza()
                exit(0)
        if i < paresN - 1:
            listapontos.append(list())

    # Printar Matriz
    print('=' * 30)
    print('Lista de Coordenadas:')
    for i in range(len(listapontos)):
        print(listapontos[i])

    return listapontos

#-----------------------------------------------------------------------------------

def paresN():
    print('=' * 30)
    while True:
        try:
            var_paresN = int(input('Qual é o número de pares de pontos (x,y)? '))
            if var_paresN < 1:
                print('Favor inserir um número inteiro positivo e não nulo.')
            else:
                break
        except ValueError:
                print('Favor inserir um número inteiro.')
    return var_paresN


def icod():
    print('=' * 30)
    print('1 = Interpolação\n2 = Regressão')
    while True:
        try:
            var_icod = int(input('Qual método será utilizado? '))
            if var_icod != 1 and var_icod != 2:
                print('Favor inserir um valor válido para o método.')
            else:
                break
        except ValueError:
            print('Favor inserir um valor válido para o método (1 ou 2)')
    return var_icod