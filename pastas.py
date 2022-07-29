import os
from datetime import date

def criarPastasDia():

    data_atual = date.today()
    ano = str(data_atual.year)
    mes = str(data_atual.month)
    dia = str(data_atual.day)

    raiz = os.getcwd()
    volta = os.path.join(raiz, "Documentos")
    os.chdir(volta)

    i = 0
    while i == 0:

        if os.path.isdir(ano):
            os.chdir(ano)

            if os.path.isdir(mes):
                os.chdir(mes)

                if os.path.isdir(dia):
                    os.chdir(dia)
                    i = 1
                else:
                    os.mkdir(dia)
                    os.chdir(volta)
            else:
                os.mkdir(mes)
                os.chdir(volta)
        else:
            os.mkdir(ano)
            os.chdir(volta)

    return os.getcwd()
