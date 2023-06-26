from lexer import *
from syntax.data_automato import *
import syntax.tres_enderecos as tres_enderecos
import semantical.semantical as semantical
from semantical.semantical import Semantical


arq = open("codigo.txt") 
linhas = arq.readlines()

i = 0
lexer = True
#leitura do arquivo de entrada
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
    if parse(l.strip(), i, j) == False:
        lexer = False
        break

verificar_tokens_desnessarios()
#vericarIds()

semantica = Semantical(TOKENS)
pda.tokenList = TOKENS
pda.linhas = linhas
pda.estadoAtual = "q0" 
a = pda.parser(0, TOKENS, "q0")

#if a != False :
#    print("erro sintático")

#for t in STM_VECTOR:
#    print(t)
#print(pda.verifica_pilha())
if len(erro_semantico) == 0 and lexer:
    if pda.verifica_pilha():
        if semantica.parser(linhas):
            tres_enderecos.clear_list()
            tres_enderecos.generate(TOKENS)
            tres_enderecos.print_code()


