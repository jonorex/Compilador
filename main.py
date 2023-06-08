from lexer import *
from syntax.data_automato import *


arq = open("codigo.txt") 
linhas = arq.readlines()

i = 0
for linha in linhas:
    l = linha
    j = 1
    for c in l:
        if c == " ":
            j = j+1
    
    i = i+1
    l = linha.strip()
    if len(l) > 0 and eUnitario(l[-1]) == False:
        linha.append("¬")
    parse(linha.strip(), i, j)

printVetor()

a = pda.parser(TOKENS)
print(a)



#print(pda.estadoAtual)

#a = validIdentifier("a")
#a = lexer.subString(code, 0, 2)

#a = eUnitario(" ")

#parse(code)
