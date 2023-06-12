from data import *
from consts import *
import copy

LEXICAL_VECTOR = []
TOKENS = []

def eUnitario(ch):

    for token in tokenList:
        if token.chave == ch and (token.tipo == DELIMITADOR or token.tipo == OP or token.tipo==SPACE):
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

def parse(code, linha, coluna): 
    left = 0 
    right = 0

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
            left = right
    
    verificaOpComposto()
    return


def isComposeOperator(a, b):
    c = a + b
    for token in tokenList:
        if token.chave == c and token.tipo == OP:
          return token 
    return False
    

def verificaOpComposto():
    s = len(LEXICAL_VECTOR)
    for i in range(s):
        if LEXICAL_VECTOR[i].tipo == OP and (i != s and i != 0):
            if LEXICAL_VECTOR[i-1].tipo == OP:
                r = copy.copy(isComposeOperator(LEXICAL_VECTOR[i-1].chave, LEXICAL_VECTOR[i].chave))
                if r != False:
                    LEXICAL_VECTOR[i-1] = r
                    LEXICAL_VECTOR[i] = TOKEN_NULO
            elif LEXICAL_VECTOR[i+1].tipo == OP:
                r = isComposeOperator(LEXICAL_VECTOR[i].chave, LEXICAL_VECTOR[i+1].chave)
                if r != False:
                    LEXICAL_VECTOR[i] = r
                    LEXICAL_VECTOR[i+1] = TOKEN_NULO
        elif i == 0 and LEXICAL_VECTOR[i+1].tipo == OP and LEXICAL_VECTOR[i] == OP:
            if LEXICAL_VECTOR[i+1].tipo == OP:
                r = isComposeOperator(LEXICAL_VECTOR[i].chave, LEXICAL_VECTOR[i+1].chave)
                if r != False:
                    
                    LEXICAL_VECTOR[i] = r
                    LEXICAL_VECTOR[i+1] = TOKEN_NULO
        elif i == s and LEXICAL_VECTOR[i-1].tipo == OP and LEXICAL_VECTOR[i].tipo == OP:
            
            if LEXICAL_VECTOR[i-1].tipo == OP:
                r = isComposeOperator(LEXICAL_VECTOR[i-1].chave, LEXICAL_VECTOR[i].chave)
                if r != False:
                    
                    LEXICAL_VECTOR[i-1] = r
                    LEXICAL_VECTOR[i] = TOKEN_NULO



def vericarIds():
    verificar_tokens_desnessarios()
    s = len(TOKENS)

    for i in range(0,s):
        if(i < s):
            print("passou aqui")
            if TOKENS[i].token == FUN.token and TOKENS[i+1].token == TOKEN_ID.token:
                TOKENS[i+1].categoria = FUNCAO
            elif TOKENS[i].tipo == TIPO and TOKENS[i+1].token == TOKEN_ID.token:
                TOKENS[i+1].categoria = VARIAVEL
    for token in TOKENS:
        print(token)
    


def verificar_tokens_desnessarios(): 
    s = len(LEXICAL_VECTOR)
    print("-------Vetor de Tokens----------\n")
    j = 0
    for i in range(s):
        if(LEXICAL_VECTOR[i] != TOKEN_NULO and LEXICAL_VECTOR[i].tipo != SPACE and LEXICAL_VECTOR[i].token != tokenList[-1].token):
            LEXICAL_VECTOR[i].id = j
            TOKENS.append(LEXICAL_VECTOR[i])
            j+=1
            


                

        


