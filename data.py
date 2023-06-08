from token_1 import Token 
from consts import *

tokenList = []
estadosFinais = []
transicoes = []




IF = Token(chave="if",token="IF",tipo=KEYWORD)
ELSE = Token(chave="else",token="ELSE",tipo=KEYWORD)
WHILE = Token(chave="while",token="WHILE",tipo=KEYWORD)
INT = Token(chave="int",token="INT",tipo=TIPO)
FLOAT =Token(chave="float",token="FLOAT",tipo=TIPO)
TRUE = Token(chave="true",token="TRUE",tipo=KEYWORD)
FALSE = Token(chave="false",token="FALSE",tipo=KEYWORD)
LONG = Token(chave="long",token="LONG",tipo=KEYWORD)
SHORT = Token(chave="short",token="SHORT",tipo=KEYWORD)
TYPEDEF = Token(chave="typedef",token="TYPEDEF",tipo=KEYWORD)
SWITCH = Token(chave="switch",token="SWITCH",tipo=KEYWORD)
TYPEDEF = Token(chave="typedef",token="TYPEDEF",tipo=KEYWORD)
VOID = Token(chave="void",token="VOID",tipo=KEYWORD)
CONST = Token(chave="const",token="CONST",tipo=KEYWORD)
BOOL = Token(chave="bool",token="BOOL",tipo=TIPO)
PRINT = Token(chave="print",token="PRINT",tipo=KEYWORD)
MAIN = Token(chave="main",token="MAIN",tipo=KEYWORD)
FOR = Token(chave="for",token="FOR",tipo=KEYWORD)
FUN = Token(chave="fun",token="FUN",tipo=KEYWORD)
MAIS = Token(chave="+",token= "MAIS",tipo= OP)
MENOS = Token(chave="-",token= "MENOS", tipo=OP)
BARRA = Token(chave="/",token= "BARRA", tipo=OP)
MAIOR = Token(chave=">", token= "MAIOR", tipo=OP)
MENOR = Token(chave="<", token= "MENOR", tipo=OP)
ASTERISCO = Token(chave="*",token= "ASTERISCO", tipo=OP)
ECOMERCIAL = Token(chave="&", token="ECOMERCIAL", tipo=OP)
IGUAL = Token(chave="=",token= "IGUAL", tipo=OP)
BARRA_RETA =Token(chave="|", token="BARRA_RETA", tipo=OP)
VIRGULA = Token(chave=",", token="VIRGULA", tipo=DELIMITADOR)
PONTO_VIRGULA = Token(chave=";", token="PONTO_VIRGULA", tipo=DELIMITADOR)
ABRE_P = Token(chave="(", token="ABRE_P", tipo=DELIMITADOR)
FECHA_P = Token(chave=")", token="FECHA_P", tipo=DELIMITADOR)
ABRE_C = Token(chave="[", token="ABRE_C", tipo=DELIMITADOR)
FECHA_C = Token(chave="]", token="FECHA_C", tipo=DELIMITADOR)
ABRE_CHAVE = Token(chave="{", token="ABRE_CHAVE", tipo=DELIMITADOR)
FECHA_CHAVE=Token(chave="}", token="FECHA_CHAVE", tipo=DELIMITADOR)
ESPACO = Token(chave=" ", token="ESPACO", tipo=SPACE)
RETURN = Token(chave="return", token="RETURN", tipo=KEYWORD)
CHAR = Token(chave="char", token="CHAR", tipo=TIPO)
IGUAL_IGUAL = Token(chave="==", token="IGUAL_IGUAL", tipo=OP)
MAIOR_IGUAL = Token(chave=">=", token="MAIOR_IGUAL", tipo=OP)
MENOR_IGUAL = Token(chave="<=", token="MENOR_IGUAL", tipo=OP)
MAIS_MAIS = Token(chave="++", token="MAIS_MAIS", tipo=OP)
MENOS_MENOS = Token(chave="--", token="MENOS_MENOS", tipo=OP)
DIFERENTE = Token(chave="!=", token="DIFERENTE", tipo=OP)
MAIOR_MAIOR = Token(chave=">>", token="RIGHT_SHIFT", tipo=OP)
MENOR_MENOR = Token(chave="<<", token="LEFT_SHIFT", tipo=OP)
MAIS_IGUAL = Token(chave="+=", token="MAIS_IGUAL", tipo=OP)
MENOS_IGUAL = Token(chave="-=", token="MENOS_IGUAL", tipo=OP)
INVERSOR = Token(chave="!", token="INVERSOR", tipo=OP)
FLEXA = Token(chave="->", token="FLEXA", tipo=OP)
DOIS_PONTOS = Token(chave=":", token="DOIS_PONTOS", tipo=OP)
DOIS_PONTOS = Token(chave=":", token="DOIS_PONTOS", tipo=DELIMITADOR)
ASPAS = Token(chave='"', token="ASPAS", tipo=DELIMITADOR)
ASPAS_SIMPLES = Token(chave="'", token="ASPAS_SIMPLES", tipo=DELIMITADOR)
COMPLETE = Token(chave="¬", token="COMPLETE", tipo=DELIMITADOR)


tokenList.append(IF)
tokenList.append(ELSE)
tokenList.append(WHILE)
tokenList.append(INT)
tokenList.append(FLOAT)
tokenList.append(TRUE)
tokenList.append(FALSE)
tokenList.append(LONG)
tokenList.append(SHORT)
tokenList.append(TYPEDEF)
tokenList.append(SWITCH)
tokenList.append(VOID)
tokenList.append(CONST)
tokenList.append(BOOL)
tokenList.append(PRINT)
tokenList.append(FOR)
tokenList.append(FUN)
tokenList.append(MAIS)
tokenList.append(MENOS)
tokenList.append(BARRA)
tokenList.append(MAIOR)
tokenList.append(MENOR)
tokenList.append(ASTERISCO)
tokenList.append(ECOMERCIAL)
tokenList.append(IGUAL)
tokenList.append(BARRA_RETA)
tokenList.append(VIRGULA)
tokenList.append(PONTO_VIRGULA)
tokenList.append(ABRE_P)
tokenList.append(FECHA_P)
tokenList.append(ABRE_C)
tokenList.append(FECHA_C)
tokenList.append(ABRE_CHAVE)
tokenList.append(FECHA_CHAVE)
tokenList.append(ESPACO)
tokenList.append(RETURN)
tokenList.append(CHAR)
tokenList.append(IGUAL_IGUAL)
tokenList.append(MAIOR_IGUAL)
tokenList.append(MENOR_IGUAL)
tokenList.append(MAIS_MAIS)
tokenList.append(MENOS_MENOS)
tokenList.append(DIFERENTE)
tokenList.append(MAIOR_MAIOR)
tokenList.append(MENOR_MENOR)
tokenList.append(MAIOR_IGUAL)
tokenList.append(MENOR_IGUAL)
tokenList.append(INVERSOR)
tokenList.append(FLEXA)
tokenList.append(DOIS_PONTOS)
tokenList.append(ASPAS)
tokenList.append(ASPAS_SIMPLES)
tokenList.append(COMPLETE)