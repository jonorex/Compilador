from lexer import *
from syntax.data_automato import *


arq = open("codigo.txt") 
linhas = arq.readlines()


for linha in linhas:
    parse(linha.strip())

printVetor()

a = pda.parser(TOKENS)
print(a)


#print(pda.estadoAtual)

#a = validIdentifier("a")
#a = lexer.subString(code, 0, 2)

#a = eUnitario(" ")

#parse(code)
