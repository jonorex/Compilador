from syntax.pda import *
from syntax.transicao import *


arq = open("automato_pda.txt")
linhas = arq.readlines()
nEstados = 40
estadoInicial = "q0"
estadosFinais = ["q0", "q15", "q26"]

transicoes = []
i = 0
for linha in linhas:
    linha.strip()
    campos  = linha.split(",", 8)
    #i = i+1
    #print(i)
    for campo in campos: 
        campo.strip()
    
    c1 = campos[1].strip()
    c3 = campos[3].strip()
    c4 = campos[4].strip()
    c5 = campos[5].strip()
    c6 = campos[6].strip()
    c7 = campos[7].strip()
    v = False
    for c in c6:
        if c == '.':
            v = True
    
    
    if v:
         c6 = c6.split(".")

    if(c7 == "0" ):
        c7 = False
    else:
        c7 = True

    if c1 == "tipo":
        c1 = TIPO
    elif c1 == "id":
        c1 = TOKEN_ID.token
    elif c1 == "num":
        c1 = TOKEN_NUMERO.token
    elif c1 == "op":
        c1 = OP


    if c3 == "tipo":
        c3 = TIPO
    elif c3 == "token":
        c3 = TOKEN

    if c4 == "igual":
        c4 = IGUAL
    elif c4 == "DIFERENTE":
        c4 = DIFERENTE
    
    if c5 == "manter":
        c5 = MANTER
    elif c5 == "emp":
        c5 = EMPILHAR
    elif c5 == "desemp":
        c5 = DESEMPILHAR
    elif c5 == "verifica":
        c5 = VER_TOPO
    elif c5 == "verEmp":
        c5 = VERIFICA_E_EMPILHA
    elif c5 == "verTopoDesempEmp":
        c5 = VERIFICA_DESEMPILHA_EMPILHA



    t = Transicao(estado_inicial = campos[0].strip(),
                  palavra_chave = c1, 
                  estado_final = campos[2].strip(), 
                  campo_analisado = c3, 
                  condicao = c4, 
                  op_pilha = c5,
                  alteracao_pilha = c6,
                  consumir= c7
                  )

    transicoes.append(t)

pda = Pda(estadoInicial= estadoInicial, 
    estadosFinais= estadosFinais, 
    nEstados= nEstados, 
    transicoes= transicoes)

#for transicao in transicoes:
#    print(transicao)