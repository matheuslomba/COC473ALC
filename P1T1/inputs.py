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

def cria_vetor(ordemN):
    vetor = []
    print('=' * 30)

    for i in range(0, ordemN):
        try:
            vetor.append(float(input('Insira um valor para o vetor B: ')))
        except ValueError:
            print("Favor rodar o programa novamente e inserir um número válido (float).")
            finaliza()
            exit(0)

    #Printar Vetor
    print('=' * 30)
    print(f'Vetor B: {vetor}')

    return vetor

#-------------------------------------


def ordemN():
    print('=' * 30)
    while True:
        try:
            var_ordemN = int(input('Qual é a ordem N do sistema de equações? '))
            if var_ordemN < 2:
                print('Favor inserir um número maior ou igual a 2.')
            else:
                break
        except ValueError:
                print('Favor inserir um número maior ou igual a 2.')
    return var_ordemN


def icod():
    print('=' * 30)
    print('1 = Decomposição LU\n2 = Decomposição de Cholesky\n3 = Procedimento Iterativo Jacobi\n4 = Procedimento Iterativo Gauss-Seidel')
    while True:
        try:
            var_icod = int(input('Qual método será utilizado? '))
            if var_icod < 1 or var_icod > 4:
                print('Favor inserir um valor válido para o método.')
            else:
                break
        except ValueError:
            print('Favor inserir um valor válido para o método (1, 2, 3 ou 4)')
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