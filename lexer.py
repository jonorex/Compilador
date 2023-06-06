from data import tokenList
from consts import *

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

def parse(code): 
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
                LEXICAL_VECTOR.append(t)
            #elif r != False:
            #    LEXICAL_VECTOR.append(r)
            right+=1
            left = right
         
        elif (eUnitario(code[right]) != False and left != right) or (right == size-1 and left != right):
            sub = code[left : right]
            r = isKeyWord(sub)
            if r != False:
                LEXICAL_VECTOR.append(r)
            elif isNumber(sub):
                LEXICAL_VECTOR.append(TOKEN_NUMERO)
            elif validIdentifier(sub) == True and eUnitario(code[right-1]) == False:
                LEXICAL_VECTOR.append(TOKEN_ID)
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
                r = isComposeOperator(LEXICAL_VECTOR[i-1].chave, LEXICAL_VECTOR[i].chave)
                if r != False:
                    LEXICAL_VECTOR[i-1] = r
                    LEXICAL_VECTOR[i] = TOKEN_NULO
            elif LEXICAL_VECTOR[i+1].tipo == OP:
                r = isComposeOperator(LEXICAL_VECTOR[i].chave, LEXICAL_VECTOR[i+1].chave)
                if r != False:
                    LEXICAL_VECTOR[i] = r
                    LEXICAL_VECTOR[i+1] = TOKEN_NULO
        elif i == 0:
            if LEXICAL_VECTOR[i+1].tipo == OP:
                r = isComposeOperator(LEXICAL_VECTOR[i].chave, LEXICAL_VECTOR[i+1].chave)
                if r != False:
                    LEXICAL_VECTOR[i] = r
                    LEXICAL_VECTOR[i+1] = TOKEN_NULO
        elif i == s:
            
            if LEXICAL_VECTOR[i-1].tipo == OP:
                r = isComposeOperator(LEXICAL_VECTOR[i-1].chave, LEXICAL_VECTOR[i].chave)
                if r != False:
                    LEXICAL_VECTOR[i-1] = r
                    LEXICAL_VECTOR[i] = TOKEN_NULO



    


def printVetor(): 
    s = len(LEXICAL_VECTOR)
    print("-------Vetor de Tokens----------\n")
    for i in range(s):
        if(LEXICAL_VECTOR[i] != TOKEN_NULO and LEXICAL_VECTOR[i].tipo != SPACE):
            TOKENS.append(LEXICAL_VECTOR[i])
            print(LEXICAL_VECTOR[i].token)


                

        


