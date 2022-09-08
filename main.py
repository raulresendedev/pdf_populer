import pdfrw
import xlrd
import os
from pastas import criarPastasDia

loc = os.path.abspath("carta_remessa.xls")

# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
linha = []
raiz = os.getcwd()
path_modelo = pdfrw.PdfReader(os.path.abspath("modelo_1.pdf"))


def gerarPdf(texto, nome):

    pdf = texto[3]+" - "+nome+".pdf"

    path_saida = criarPastasDia()+"\\"+pdf

    for page in path_modelo.Root.Pages.Kids:
        for i, field in enumerate(page.Annots):
            field.V = str(texto[i])

    path_modelo.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))

    pdfrw.PdfWriter().write(path_saida, path_modelo)

    os.chdir(raiz)

print("========================GERAR CARTAS REMESSAS========================")
op = input("DESEJA PROSSEGUIR? S / N: ").upper()
if op == "S":
    for l in range(sheet.nrows):
        for c in range(sheet.ncols):
            linha.append(sheet.cell_value(l, c))
        if l != 0:
            nome = str(linha[1])
            endereco = str(linha[1])+", CPF: "+str(linha[2])+", TELEFONE: "+str(linha[3])+", situanda na "+str(linha[4])
            linha.pop(1)
            linha.pop(1)
            linha.pop(1)
            linha.pop(1)
            linha.insert(1, endereco)
            linha[3] = str(linha[3])
            gerarPdf(linha, nome)
        linha.clear()
else:
    print("Encerrado!")