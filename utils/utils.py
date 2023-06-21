from consts import OP
RESULT = []
from data import tokenList
from consts import *
from data import *

def gerar_menssagem_erro(tipo, token, linha):
    linha_numerica = token.linha
    coluna = token.coluna
    if token.nome == "":   
        nome_token = token.nome
    else:
        nome_token = token.chave
    string_error = ""
    titulo = "Erro "+ tipo + " na linha: "+ str(linha_numerica)
    print(titulo)
    linha =  linha.replace("\n", "")
    print(linha)
    for i in range(0, coluna-1):
        string_error+="-"
    for i in range(0,len(nome_token)):
        string_error+= "∧"
    
    
    print(string_error)

def gerar_menssagem_erro_tipos_incompativeis(l_token, r_token, linha):
    print("Tipos incompátiveis na linha "+ str(r_token.linha+1)+": ")
    linha = linha.replace("\n", "")
    print(linha)
    if r_token.nome == "":
        nome = r_token.chave
    else: nome = r_token.nome   
    string_error = ""
    for i in range(0, r_token.coluna-1):
        string_error+="-"
    for i in range(0,len(nome)):
        string_error+= "∧"
    print(string_error)
    print("Era esperado um valor do tipo "+ l_token.tipo_dado + ", mas o tipo foi obtido foi "+ r_token.tipo_dado)
    print("\n")

def gerar_menssagem_erro_sintatico(token_lido, tokens_esperado, linha):
    if token_lido.linha == 0:
        return ""
    text = ""
    text +="Erro sintático na linha "+ str(token_lido.linha+1) + ": "
    #print("token_lido ",token_lido)
    text +="\n"
    linha = linha.replace("\n", "")
    text+=linha
    string_error = ""
    for i in range(0, token_lido.coluna-1):
        string_error+="-"
    if token_lido.tipo == OP:
        for i in range(0,len(token_lido.chave)):
            string_error+= "∧"
    else:
        for i in range(0,len(token_lido.nome)):
            string_error+= "∧"    
    text += "\n"
    text += string_error
    text += "\n"
    text += "Os tokens esperados são : "
    for t in tokens_esperado:
        text += t.palavra_chave +", "
    text += "\n"
    text += "Porém foi lido um "+str(token_lido.token)

    print(text)


def gerar_menssagem_erro_sintatico_token_exedido(token, linha):
    if token.linha == 0:
        return ""
    text = ""
    text+= "token exedido na linha "+str(token.linha)
    text+= "\n"
    text+= linha
    string_error = ""
    for i in range(0, token.coluna-1):
        string_error+="-"
    if token.tipo == OP:
        for i in range(0,len(token.chave)):
            string_error+= "∧"
    else:
        for i in range(0,len(token.nome)):
            string_error+= "∧"    
    text += "\n"
    return text



def encontrar_token(s_token):
    if s_token == TIPO: 
        return INT
    elif s_token == TOKEN_ID.token:
        return TOKEN_ID
    elif s_token == TOKEN_NUMERO.token:
        return TOKEN_NUMERO
    elif s_token == OP:
        return MAIS
    for token in tokenList:
        if s_token ==  token.token:
            return token


