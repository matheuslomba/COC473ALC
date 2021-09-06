from inputs import icod, tolM, c1234
from metodos1 import raiz
from metodos2 import integral
from metodos3 import derivadaDF
from metodos4 import derivadaRE
from sup import finaliza

#Inputs do programa
c, d, e, f = c1234()
var_icod = icod()

if var_icod == 1:
    var_tolM = tolM()
    raiz(c, d, e, f, var_tolM)
elif var_icod == 2:
    integral(c, d, e, f)
elif var_icod == 3:
    derivadaDF(c, d, e, f)
elif var_icod == 4:
    derivadaRE(c, d, e, f)

finaliza()