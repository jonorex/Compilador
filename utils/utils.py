
RESULT = []



def gerar_menssagem_erro(tipo, token, linha):
    linha_numerica = token.linha
    coluna = token.coluna
    nome_token = token.nome
    string_error = ""
    titulo = "Erro "+ tipo + " na linha: "+ str(linha_numerica)
    print(titulo)
    print(linha)
    for i in range(0, coluna-1):
        string_error+="-"
    for i in range(0,len(nome_token)):
        string_error+= "∧"
    
    print(string_error)
    



def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    """Implementa pesquisa binária recursivamente."""
    # 1. Caso base: o elemento não está presente. 
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo. 
    if A[meio].id == item.id:
        RESULT.append[meio]
        return meio
    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca. 
    elif A[meio].id >= item.id:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else: # A[meio] < item
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)