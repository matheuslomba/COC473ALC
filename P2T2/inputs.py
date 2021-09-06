from sup import finaliza


# ====================
# Inputs gerais

def c1234():
    print('=' * 30)
    while True:
        try:
            c = float(input('Qual será o valor de c1? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            d = float(input('Qual será o valor de c2? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            e = float(input('Qual será o valor de c3? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            f = float(input('Qual será o valor de c4? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    return c, d, e, f


def icod():
    print('=' * 30)
    print('1 = Raiz\n2 = Integral\n3 = Derivada DF\n4 = Derivada RE')
    while True:
        try:
            var_icod = int(input('Qual método será utilizado? '))
            if var_icod != 1 and var_icod != 2 and var_icod != 3 and var_icod != 4:
                print('Favor inserir um valor válido para o método.')
            else:
                break
        except ValueError:
            print('Favor inserir um valor válido para o método (1, 2, 3 ou 4)')
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


# ====================
# Inputs: Raiz - Método Bisseção; Integral - Quadratura de Gauss
def ab():
    print('=' * 30)
    while True:
        try:
            a = float(input('Qual será o valor de a? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    while True:
        try:
            b = float(input('Qual será o valor de b? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    return a, b


# Inputs: Raiz - Método Newton
def x_inicial():
    print('=' * 30)
    while True:
        try:
            x_ini = float(input('Qual será o valor inicial de x (x0)? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    return x_ini


# Inputs: Raiz - Método Newton
def maxIter():
    print('=' * 30)
    while True:
        try:
            max_it = int(input('Qual será o número máximo de iterações? '))
            break
        except ValueError:
            print('Favor inserir um número inteiro.')
    return max_it


# Inputs: Integral - Quadratura de Gauss
def num_pontos():
    print('=' * 30)
    while True:
        try:
            n_pts = int(input('Qual é o número de pontos que serão usados? (entre 2 e 10) '))
            if n_pts < 2 or n_pts > 10:
                print('Favor inserir um valor válido para o método.')
            else:
                break
        except ValueError:
            print('Favor inserir um número inteiro.')
    return n_pts


# Inputs: DerivadaDF
def pontox():
    print('=' * 30)
    while True:
        try:
            x = float(input('Deseja calcular a derivada de f em que ponto x? '))
            break
        except ValueError:
            print('Favor inserir um número float.')
    return x


def deltax(n):
    print('=' * 30)
    while True:
        try:
            if n == 0:
                dx = float(input('Qual é o valor de delta x? '))
                break
            elif n == 1:
                dx = float(input('Qual é o valor de delta x1? '))
                break
            elif n == 2:
                dx = float(input('Qual é o valor de delta x2? '))
                break
        except ValueError:
            print('Favor inserir um número float.')
    return dx

