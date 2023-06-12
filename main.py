from lexer import *
from syntax.data_automato import *
from syntax.arvore import *
from syntax.tres_enderecos import *


arq = open("codigo.txt") 
linhas = arq.readlines()

i = 0
for linha in linhas:
    l = linha
    j = 1
    for c in l:
        if c.isalpha() or c.isnumeric():
            break
        if c == " ":
            j = j+1
    i = i+1
    l = linha.strip()
    if len(l) > 0 and eUnitario(l[-1]) == False:
        l = l + "¬"
    parse(l.strip(), i, j)

vericarIds()



a = pda.parser(TOKENS)
print(a)

##for t in TRANSICOES:
##    if t.condicao == IGUAL:
##        print(t.estado_inicial)
print("STM_VECTOR")
for stm in STM_VECTOR:
    print(stm)



##for t in  pda.transicoes:
##    print(t)
#
#
##print("linha 36", len(STM_VECTOR))
##v = Stm(STM_VECTOR=STM_VECTOR)
##v.reduzir_expressao(TOKENS, 0, 0)
#tres =Tres()
#tres.gerarChamadaFuncao(TOKENS)
##tres.reduzir()
#tres.verificar_exp(TOKENS)

#print(TOKENS[-2])
#print(TOKENS[-3])
#print(pda.estadoAtual)

#a = validIdentifier("a")
#a = lexer.subString(code, 0, 2)

#a = eUnitario(" ")

#parse(code)
