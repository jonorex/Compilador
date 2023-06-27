from data import *
from consts import *
import copy
import utils.utils as utils

LEXICAL_VECTOR = []
TOKENS = []
LISTA_FUNCOES_E_VARIAVEIS =[]

class Comment:
    def __init__(self) -> None:
        self.is_comment = False
    
    def set_comment(self):
        if self.is_comment:
            self.is_comment = False
        else:
            self.is_comment = True


comment = Comment()

def eUnitario(ch):
    for token in tokenList:
        if token.chave == ch and (token.tipo == DELIMITADOR or token.tipo == OP or token.tipo==SPACE or token.tipo == "ATRIB"):
          return token 
    return False

def eDelimitador(ch):
    for token in tokenList:
        if (token.chave == ch or token.token == ch) and token.tipo == DELIMITADOR:
            return token
    return False

def validIdentifier(subStr):
    if subStr[0].isnumeric() or eDelimitador(subStr[0]) != False:
        return False
    size = len(subStr)
    if size == 1:
        return True
    else:
        for i in range(size):
            if(eDelimitador(subStr[i]) != False):
                return False
            
    return True

def isOperator(ch):
    for token in tokenList:
        if token.chave == ch and token.tipo == OP:
            return token
    return False

def isKeyWord(subStr):
    for token in tokenList:
        if token.chave == subStr and (token.tipo == KEYWORD or token.tipo == TIPO):
            return token

    return False

def isNumber(stri):
    if stri.isnumeric():
        return True
    else:
        return False
    
def isFloat(stri):
    sp = stri.split(".")
    if len(sp) == 2 and sp[0].isnumeric() and sp[1].isnumeric():
        return True
    else: return False

def isBooleanValue(stri):
    if stri == TRUE.chave or stri == FALSE.chave:
        return True
    else: return False
        

def parse(code, linha, coluna): 
    left = 0 
    right = 0
    comment.is_comment = False
    size = len(code)
    while right <= size-1 and left <= right:
        if eUnitario(code[right]) == False: 
            right+= 1
        if eUnitario(code[right]) != False and left == right:
            s = isOperator(code[right])
            r = eDelimitador(code[right])
            t = eUnitario(code[right])
            if t != False:
                dl = copy.copy(t)
                dl.linha = linha
                dl.coluna = coluna+left
                LEXICAL_VECTOR.append(dl)
            #elif r != False:
            #    LEXICAL_VECTOR.append(r)
            right+=1
            left = right
         
        elif (eUnitario(code[right]) != False and left != right) or (right == size-1 and left != right):
            sub = code[left : right]
            r = isKeyWord(sub)
            if r != False:
                k = copy.copy(r)
                k.linha = linha
                k.coluna = coluna+left
                LEXICAL_VECTOR.append(k)
            elif isNumber(sub):
                num = copy.copy(TOKEN_NUMERO)
                num.linha = linha
                num.coluna = coluna+left
                num.nome = sub
                num.tipo_dado = "INT"
                LEXICAL_VECTOR.append(num)
            elif isFloat(sub):
                num = copy.copy(TOKEN_NUMERO)
                num.linha = linha
                num.coluna = coluna+left
                num.nome = sub
                num.tipo_dado = "FLOAT"
                LEXICAL_VECTOR.append(num)
            elif isBooleanValue(sub):
                num = copy.copy(TOKEN_NUMERO)
                num.linha = linha
                num.coluna = coluna+left
                num.nome = sub
                num.tipo_dado = "BOOL"
                LEXICAL_VECTOR.append(num)
            elif validIdentifier(sub) == True and eUnitario(code[right-1]) == False:
                tId = copy.copy(TOKEN_ID) 
                tId.linha = linha
                tId.coluna = coluna + left
                tId.nome = sub
                LEXICAL_VECTOR.append(tId)
            elif validIdentifier(sub) == False and eUnitario(code[right-1]) == False:
                tId = copy.copy(TOKEN_ID) 
                tId.linha = linha
                tId.coluna = coluna + left
                tId.nome = sub
                LEXICAL_VECTOR.append(tId)
                utils.gerar_menssagem_erro("Erro léxico identificador inválido: ", tId, code)
                return False
            left = right
    
    verificaOpComposto()
    isCharValue()
    return

def isLogicOperator(): #verifica se o tipo do operador depois de fazer o parse de todas as linhas
    for token in TOKENS:
        if token.token == MAIS.token or token.token == MENOS.token or token.token == ASTERISCO.token or token.token == BARRA.token:
            token.categoria = "math"
        elif  token.token == AND.token or token.token == OR.token:
            token.categoria = "logic" 
        elif token.token == MAIOR.token or token.token == MENOR.token or token.token == MAIOR_IGUAL.token or token.token == MENOR_IGUAL.token:
            token.categoria = "relacional"

def isComposeOperator(a, b):#verifica se o tipo do operador é composto depois de fazer o parse de todas as linhas
    c = a + b
    for token in tokenList:
        if token.chave == c and token.tipo == OP:
          return token 
    return False
def isCharValue(): #verifica se o valor é char
    i = 0
    while i < len(LEXICAL_VECTOR):
        if LEXICAL_VECTOR[i].token == ASPAS_SIMPLES.token and LEXICAL_VECTOR[i+2].token == ASPAS_SIMPLES.token:
            
            value = LEXICAL_VECTOR[i+1].nome
            if LEXICAL_VECTOR[i+1].nome == "":
                value = LEXICAL_VECTOR[i+1].chave
            num = copy.copy(TOKEN_NUMERO) # o token numero é utilizado para representar qualquer tipo de valor a propriedade que armazena o tipo é o atributo tipo_dado
            num.linha = LEXICAL_VECTOR[i].linha
            num.coluna = LEXICAL_VECTOR[i].coluna
            num.nome = ASPAS_SIMPLES.chave+value+ASPAS_SIMPLES.chave
            num.tipo_dado = "CHAR"
            LEXICAL_VECTOR[i]=num
            LEXICAL_VECTOR[i+1] = TOKEN_NULO
            LEXICAL_VECTOR[i+2] = TOKEN_NULO

        elif  LEXICAL_VECTOR[i].token == ASPAS.token and LEXICAL_VECTOR[i+2].token == ASPAS.token:
            value = LEXICAL_VECTOR[i+1].nome
            if LEXICAL_VECTOR[i+1].nome == "":
                value = LEXICAL_VECTOR[i+1].chave
            num = copy.copy(TOKEN_NUMERO)
            num.linha = LEXICAL_VECTOR[i].linha
            num.coluna = LEXICAL_VECTOR[i].coluna
            num.nome = ASPAS.chave+value+ASPAS.chave
            num.tipo_dado = "CHAR"
            LEXICAL_VECTOR[i]=num
            LEXICAL_VECTOR[i+1] = TOKEN_NULO
            LEXICAL_VECTOR[i+2] = TOKEN_NULO
        i+=1

def verificaOpComposto(): #após a análise é verificado se dois operadores que estão juntos possam ser compostos com  && >=
    s = len(LEXICAL_VECTOR)
    for i in range(s):
        #print(LEXICAL_VECTOR[i])
        if (LEXICAL_VECTOR[i].tipo == OP or LEXICAL_VECTOR[i].tipo == OP_ATR) and (i != s and i != 0):
            if LEXICAL_VECTOR[i-1].tipo == OP or LEXICAL_VECTOR[i-1].tipo == OP_ATR:
                r = copy.copy(isComposeOperator(LEXICAL_VECTOR[i-1].chave, LEXICAL_VECTOR[i].chave))
                if r != False:
                    LEXICAL_VECTOR[i-1] = r
                    LEXICAL_VECTOR[i] = TOKEN_NULO
            elif LEXICAL_VECTOR[i+1].tipo == OP or LEXICAL_VECTOR[i+1].tipo == OP_ATR:
                r = isComposeOperator(LEXICAL_VECTOR[i].chave, LEXICAL_VECTOR[i+1].chave)
                if r != False:
                    LEXICAL_VECTOR[i] = r
                    LEXICAL_VECTOR[i+1] = TOKEN_NULO
        elif i == 0 and (LEXICAL_VECTOR[i+1].tipo == OP or LEXICAL_VECTOR[i+1].tipo == OP_ATR) and (LEXICAL_VECTOR[i] == OP or LEXICAL_VECTOR[i].tipo == OP_ATR):
            if LEXICAL_VECTOR[i+1].tipo == OP or LEXICAL_VECTOR[i+1].tipo == OP_ATR:
                r = isComposeOperator(LEXICAL_VECTOR[i].chave, LEXICAL_VECTOR[i+1].chave)
                if r != False:     
                    LEXICAL_VECTOR[i] = r
                    LEXICAL_VECTOR[i+1] = TOKEN_NULO
        elif i == s and (LEXICAL_VECTOR[i-1].tipo == OP or LEXICAL_VECTOR[i-1].tipo == OP_ATR) and (LEXICAL_VECTOR[i].tipo == OP or LEXICAL_VECTOR[i].tipo == OP_ATR):
            
            if LEXICAL_VECTOR[i-1].tipo == OP or LEXICAL_VECTOR[i-1].tipo == OP_ATR:
                r = isComposeOperator(LEXICAL_VECTOR[i-1].chave, LEXICAL_VECTOR[i].chave)
                if r != False:
                    LEXICAL_VECTOR[i-1] = r
                    LEXICAL_VECTOR[i] = TOKEN_NULO
        if i != s and LEXICAL_VECTOR[i].token == MENOS.token and LEXICAL_VECTOR[i+1].token == TOKEN_NUMERO.token:
            LEXICAL_VECTOR[i+1].nome = "-"+ LEXICAL_VECTOR[i+1].nome
            LEXICAL_VECTOR[i+1].coluna -= 1
            LEXICAL_VECTOR[i] = TOKEN_NULO

#retira tokens que nao sao uteis na analise como espacos 
def verificar_tokens_desnessarios(): 
    s = len(LEXICAL_VECTOR)
    #print("-------Vetor de Tokens----------\n")
    j = 0
    for i in range(s):
        if(LEXICAL_VECTOR[i] != TOKEN_NULO and LEXICAL_VECTOR[i].tipo != SPACE and LEXICAL_VECTOR[i].token != tokenList[-1].token):
            LEXICAL_VECTOR[i].id = j
            TOKENS.append(LEXICAL_VECTOR[i])
            j+=1


    isLogicOperator()
    
            


                

        


