from sup import finaliza

def cria_matriz(ordemN):
    matriz = [[]]
    print('=' * 30)

    for i in range(0, ordemN):
        for j in range(0, ordemN):
            try:
                matriz[i].append(float(input(f'Insira um valor para A({i+1},{j+1}): ')))
            except ValueError:
                print("Favor rodar o programa novamente e inserir um número válido (float).")
                finaliza()
                exit(0)
        if i < ordemN-1:
            matriz.append(list())

    #Printar Matriz
    print('='*30)
    print('Matriz A:')
    for i in range(len(matriz)):
        print(matriz[i])

    return matriz

#-------------------------------------

def ordemN():
    print('=' * 30)
    while True:
        try:
            var_ordemN = int(input('Qual é a ordem N do sistema de equações? '))
            if var_ordemN < 1:
                print('Favor inserir um número inteiro positivo e não nulo.')
            else:
                break
        except ValueError:
                print('Favor inserir um número inteiro.')
    return var_ordemN


def icod():
    print('=' * 30)
    print('1 = Método da Potência\n2 = Método de Jacobi')
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


def idet():
    print('=' * 30)

    while True:
        var_idet = str(input('Deseja calcular a determinante da Matriz A? (s/n) '))
        if var_idet.lower() != 's' and var_idet.lower() != 'n':
            print('Favor inserir uma resposta válida (s/n).')
        else:
            if var_idet.lower() == 's':
                return True
            else:
                return False


def tolM():
    print('=' * 30)
    while True:
        try:
            var_tolM = float(input('Qual será a tolerância máxima para a solução iterativa? '))
            break
        except ValueError:
                print('Favor inserir um número float.')
    return var_tolM