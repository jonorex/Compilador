from token_1 import Token

EMPILHAR = "emp"
DESEMPILHAR = "desemp"
MANTER = "manter"
PILHA_VAZIA = "pilha_vazia"
VER_TOPO = "ver_topo"

TOKEN_NUMERO = Token(chave="", token="NUMERO", tipo="")
TOKEN_ID = Token(chave="", token="IDENTIFICADOR", tipo="")
VARIAVEL = "var"
FUNCAO = "fun"
TOKEN_INVALID_ID = Token(chave="", token="IDENTIFICADOR_INVALIDO", tipo="")

DELIMITADOR = "DELIMITADOR"
OP = "operador"
OP_ATR = "ATRIB"
SPACE = "SPACE"
KEYWORD = "keyWord"
TIPO = "TIPO"
OP_COMPOSTO = "token_composto"
IGUAL = "IGUAL"
DIFERENTE = "DIFERENTE"
TOKEN = "TOKEN"
TOKEN_NULO = Token(chave="", token="TOKEN_NULO", tipo="")
VERIFICA_E_EMPILHA = "verEmp"
VERIFICA_DESEMPILHA_EMPILHA = "verTopoDesempEmp"