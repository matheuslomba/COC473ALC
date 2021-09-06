from sup import finaliza


def recebeParams():
    print('=' * 30)
    while True:
        try:
            teta1 = float(input('Qual é o valor do primeiro parametro que será usado na solução? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    print('=' * 30)
    while True:
        try:
            teta2 = float(input('Qual é o valor do segundo parametro que será usado na solução? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    return teta1, teta2


def criaVetor():
    vetor = []
    print('=' * 30)

    for i in range(0, 3):
        try:
            vetor.append(float(input('Insira um valor para o vetor X[' + str(i + 1) + ']: ')))
        except ValueError:
            print("Favor rodar o programa novamente e inserir um número válido (float).")
            finaliza()
            exit(0)

    # Printar Vetor
    print('=' * 30)
    print('Vetor X: ' + str(vetor))

    return vetor


def icod():
    print('=' * 30)
    print('1 = Método de Newton\n2 = Método de Broyden')
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


def tolM():
    print('=' * 30)
    while True:
        try:
            var_tolM = float(input('Qual será a tolerância máxima para a solução iterativa? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    return var_tolM