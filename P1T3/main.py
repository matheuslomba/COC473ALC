from inputs import pontox, coordenadas, paresN, icod
from metodos import interpolacao, regressao
from sup import finaliza

#Inputs do programa
var_paresN = paresN()
var_icod = icod()
x = pontox()
listapontos = coordenadas(var_paresN)


if var_icod == 1:
    interpolacao(x, listapontos, var_paresN)
elif var_icod == 2:
    regressao(x, listapontos, var_paresN)

finaliza()