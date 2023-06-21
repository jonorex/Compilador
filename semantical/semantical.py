from data import *
SUB = [FUN, WHILE, IF, ELSE]
import copy
import utils.utils as utils
LISTA_FUNCOES_E_VARIAVEIS = []
from syntax.tres_enderecos import *
from syntax.pda import STM_VECTOR
class Semantical:
    def __init__(self, TOKENS) -> None:
        self.TOKENS = TOKENS
        self.funcoes = []
    def buscar_abre_chave(self):
        lista = []
        i = - 1
        for token in STM_VECTOR:
            i+=1
            if token.token == ABRE_CHAVE.token:
                lista.append([token, i])
        return lista

    def buscar_tokens_de_sub_escopo(self, abre_chave):
        i = abre_chave.id
        #print("abre_chave id", i)

        while i > -1:
            if self.TOKENS[i].token == FUN.token:
                sub = self.TOKENS[i]
                break
            elif self.TOKENS[i].token == IF.token:
                sub = self.TOKENS[i]
                break
            elif self.TOKENS[i].token == WHILE.token:
                sub = self.TOKENS[i]
                break
            elif self.TOKENS[i].token == ELSE.token:
                sub = self.TOKENS[i]
                break
            #print(TOKENS[i].token)
            i-=1  
        return sub

    def definir_escopo(self, token_sub, abre_chave):
       # print("40 ",abre_chave[1])
        a = abre_chave[1]
        fecha_chave = STM_VECTOR[a+1]

        lista = []

        #print("token_sub ", token_sub)

        #print("linha 43 ",fecha_chave.id)
        i = abre_chave[0].id
        s = fecha_chave.id
        while i < s:
            a = token_sub.token + " " +str(token_sub.id) + ","
            self.TOKENS[i].escopo += a 
            i+=1


    def buscar_tokens(self):
        lista_abre_chave = self.buscar_abre_chave()

        #print(lista_abre_chave)

        for abre_chave in lista_abre_chave:
            sub = self.buscar_tokens_de_sub_escopo(abre_chave[0])
            self.definir_escopo(sub, abre_chave)
        
        self.categorizar_identificadores()


    def buscar_ids(self, t_id):
        
        a = t_id.id
        b = len(self.TOKENS)
        for i in range(0, b):  
            t = self.TOKENS[i]
            sp = t_id.categoria.split(" ")
            categoria_child = t.categoria.split(" ")
            #print("cc",categoria_child)
            if t.nome == t_id.nome and sp[0] != "ref" and categoria_child[0] != "var" and categoria_child[0] != "fun":
                #print("linha 92", t)
                self.verificar_escopo(t_id, t)
            
    def verificar_escopo(self, parent, child):
        ps = parent.escopo.split(",")
        cs = child.escopo.split(",")
        #print("103 ps", ps)
        if ps == cs: #identificadores estão exatamente no mesmo escopo
            child.categoria = "ref "+parent.categoria
            child.tipo_dado = parent.tipo_dado
            return
        #verifica se o parent está em escopo superior
        for st in ps:
            for st1 in cs:
                if st == st1:
                     child.categoria = "ref "+parent.categoria
                     child.tipo_dado = parent.tipo_dado
                     return

    #identifica os identicadores que vem de declaração de funções ou de variáveis
    def categorizar_identificadores(self):
        for token in self.TOKENS:
            split = token.categoria.split(",")
            #print(token.token +" == "+ TOKEN_ID.token + " and "+ token.categoria +" != '' and "+split[0] +" != ref")
            if token.token == TOKEN_ID.token and token.categoria != "" and split[0] != "ref":
                self.buscar_ids(token)
                #print("120 passou aqui")
    
    
    def verificar_duplicidade(self, var, linhas):
        for t in LISTA_FUNCOES_E_VARIAVEIS:
            #print(t.nome+ " == "+ var.nome +" and "+ t.escopo +" == "+var.escopo +" and "+str(t.id)+ " != "+ str(var.id))
            if t.nome == var.nome and t.escopo == var.escopo and t.id != var.id:
                s = t.categoria.split()
                if s[0] == "fun":
                    utils.gerar_menssagem_erro("semantico duplicidade de função", var, linhas[var.linha-1])
                    return False
                elif s[0] == "var":
                    utils.gerar_menssagem_erro("semantico duplicidade de variável", var, linhas[var.linha-1])
                    return False
        return True

    def definir_escopo_args(self):
        for fun in self.funcoes:
            if len(fun[1])>0:
                for param in fun[1]:
                    a = self.TOKENS[fun[0].id-1].token + " " +str(self.TOKENS[fun[0].id-1].id) + ","
                    self.TOKENS[param.id].escopo += a 

    def buscar_fechap(self, abre_p):
        i = -1
        for st in STM_VECTOR:
            i+=1
            if st == abre_p:
                break
        return STM_VECTOR[i+1]

    def parser(self, linhas):
        self.vericarIds(linhas)
        self.buscar_tokens()
        self.definir_escopo_args()

        self.identificadores_nao_declarados(linhas)

        self.duplicidade(linhas)
        for i in range(len(self.TOKENS)):
            if self.TOKENS[i].token == IGUAL.token:
                l_value = self.TOKENS[i-1]
                j = i+1

                r_value = []
                while self.TOKENS[j].token != PONTO_VIRGULA.token:
                    if self.TOKENS[j].token == TOKEN_ID.token and self.TOKENS[j+1].token == ABRE_P.token:
                        r_value.append(self.TOKENS[j])
                        fecha_p = self.buscar_fechap(self.TOKENS[j+1])
                        j = fecha_p.id
                    else:
                        r_value.append(self.TOKENS[j])
                    j+=1
               # r_value = self.TOKENS[i+1:j]
                self.verificar_tipo(identificador=l_value, dado=r_value, linha= linhas)
    
        #self.duplicidade(linhas)
        
        self.buscar_retorno_funcao(linhas)

        self.verificar_chamada_de_funcoes(linhas)

        print("----------------____________________________")
        for t in self.TOKENS:
            print(t)
    

    def get_params(self, abreP, fechaP):
        i = abreP.id
        s = fechaP.id
        j = 0
        params = self.TOKENS[abreP.id:fechaP.id+1]
        sub = []
        #print("179 params ",params)

        #while i < s:
        #    i+= 1
        #    params.append(self.TOKENS[i])

        size  = len(params)
        for k in range(size):
            if params[k].token == VIRGULA.token or params[k].token == FECHA_P.token:
                d = k-(j+1)
                #print("linha 175 d = ",d)
                sub.append(params[j+1:k]) 
                j=k
        #print("sub 191 ", sub)
        return sub

        

    def verificar_params(self, call, linhas):
        #print("linha 198 ", call)
        call_id = call[0]
        call_params = call[1] # lista de parametros
        
        for fun in self.funcoes:
            #print("linha 205", fun)
            if fun[0].nome == call_id.nome:
                if len(call_params) == len(fun[1]):
                    i = 0 
                    for i in range(len(fun[1])):
                        self.verificar_tipo(fun[1][i], call_params[i], linhas)
                else:
                    utils.gerar_menssagem_erro("A função precisa de "+ str(len(fun[1]))+", parametros porém foram passados "+str(len(call_params)), call_id, linhas[call_id.linha - 1])
                    
            
    def verificar_chamada_de_funcoes(self, linhas):
        indices_delete = []
        for i in range(len(STM_VECTOR)):
            if STM_VECTOR[i].token == TOKEN_ID.token and STM_VECTOR[i+1].token == ABRE_P.token:
                sp =  STM_VECTOR[i].categoria.split(" ")
                #print("linha 220", sp)
                if(sp[1] ==  "fun"):
                    identificador_call = STM_VECTOR[i]  
                    params = self.get_params(STM_VECTOR[i+1], STM_VECTOR[i+2])
                    #print("linha 217 passou aqui", params)
                    self.verificar_params([identificador_call, params], linhas)
                elif(sp[1] == "var"):
                    if(self.tem_virgula(STM_VECTOR[i+1], STM_VECTOR[i+2])):
                        utils.gerar_menssagem_erro("Função "+STM_VECTOR[i].nome+" não declada", STM_VECTOR[i], linhas[STM_VECTOR[i].linha -1 ])
                        indices_delete.append(i)
                    else: 
                        ind = STM_VECTOR[i].id
                        self.TOKENS.insert(ind+1, ASTERISCO)
                        indices_delete.append(i)

        for ind in indices_delete:
            del STM_VECTOR[ind]
            del STM_VECTOR[ind]
            del STM_VECTOR[ind]
                
                
    def tem_virgula(self, abreP, fechaP):
        i = abreP.id
        s = fechaP.id

        while i < s:
            i+=1
            if self.TOKENS[i].token == VIRGULA.token:
                return True
        return False

        
    
    def buscar_tipo_funcao(self, parenteses):
        for i in range(len(STM_VECTOR)):
            if STM_VECTOR[i] == parenteses:
                fecha_p = STM_VECTOR[i+1]
        return self.TOKENS[fecha_p.id+2]
    

    def get_expressao(self, l_value, inicio, fim, token_inicial, token_final, linhas):
        i = inicio
        s = fim
        r_value = []
        tem_retorno = False
        while i < s:
            if self.TOKENS[i].token == token_inicial.token:
                tem_retorno = True
                #l_value = self.TOKENS[i-1]
                j = i
                while self.TOKENS[j].token != token_final.token:
                    j+=1
                r_value = self.TOKENS[i+1:j]
                self.verificar_tipo(identificador=l_value, dado=r_value, linha= linhas)
            i+=1
        if tem_retorno == False and l_value.tipo_dado != VOID.token:
            utils.gerar_menssagem_erro("Função do tipo "+ l_value.tipo_dado + " sem retorno", l_value, linhas[l_value.linha -1 ])
        



        
    def buscar_retorno_funcao(self, linha):
        s = len(self.TOKENS)
        i = 0
        for fun in self.funcoes:
            #print("191", fun)
            tipo_funcao = self.buscar_tipo_funcao(self.TOKENS[fun[0].id+1])
            chaves = self.encontrar_abre_chave(tipo_funcao)
           # print("192", chaves)
            self.get_expressao(fun[0], chaves[0].id, chaves[1].id, RETURN, PONTO_VIRGULA, linha)
             # self.encontrar_retornos(abre_chave)

    
 
    def encontrar_abre_chave(self, p):
        abre_chave = self.TOKENS[p.id + 1]
        s = len(STM_VECTOR)
        for i in range(s):
            if STM_VECTOR[i] == abre_chave:
                return [abre_chave, STM_VECTOR[i+1]]
        

    def getArgs(self, fun):
        i =fun.id+1
        args = []
        
        while self.TOKENS[i].token != FECHA_P.token:
            i+=1
            if self.TOKENS[i].tipo == TIPO or self.TOKENS[i].token == FECHA_P.token or self.TOKENS[i].token == VIRGULA.token:
                continue

            args.append(self.TOKENS[i])
        #print("args",args)
        return args
         

    def vericarIds(self, linhas):
        s = len(self.TOKENS)
        b = True
        for i in range(0,s):
            if(i < s):
                #print("passou aqui")
                if self.TOKENS[i].token == FUN.token and self.TOKENS[i+1].token == TOKEN_ID.token:
                    args = self.getArgs(self.TOKENS[i+1])
                    self.funcoes.append([self.TOKENS[i+1], args])
                    self.TOKENS[i+1].categoria = FUNCAO+" "+str(self.TOKENS[i+1].id)
                    self.TOKENS[i+1].tipo_dado = self.buscar_tipo_funcao(self.TOKENS[i+2]).token
                elif self.TOKENS[i].tipo == TIPO and self.TOKENS[i+1].token == TOKEN_ID.token:
                    if(self.TOKENS[i].token == VOID.token):
                        utils.gerar_menssagem_erro("Void é inválido para variáveis ", self.TOKENS[i], linhas[self.TOKENS[i].linha -1])
                    self.TOKENS[i+1].categoria = VARIAVEL +" "+str(self.TOKENS[i+1].id)
                    self.TOKENS[i+1].tipo_dado = self.TOKENS[i].token
        return b
    

    def duplicidade(self, linhas):
        s = len(self.TOKENS)
        b = True
        for i in range(0,s):
            if(i < s):
                #print("passou aqui")
                if self.TOKENS[i].token == FUN.token and self.TOKENS[i+1].token == TOKEN_ID.token:
                    if self.verificar_duplicidade(self.TOKENS[i+1], linhas):
                        LISTA_FUNCOES_E_VARIAVEIS.append(self.TOKENS[i+1])
                    else: b=False
                elif self.TOKENS[i].tipo == TIPO and self.TOKENS[i+1].token == TOKEN_ID.token:
                    if self.verificar_duplicidade(self.TOKENS[i+1], linhas):
                        LISTA_FUNCOES_E_VARIAVEIS.append(self.TOKENS[i+1])
                    else: b=False
        return b
    
    def identificadores_nao_declarados(self, linhas):
        r = True
        for i in range(len(self.TOKENS)):
            if self.TOKENS[i].categoria == "" and self.TOKENS[i].token == TOKEN_ID.token:
                r = False
                if self.TOKENS[i+1].token == ABRE_P.token:
                    utils.gerar_menssagem_erro("Função "+ self.TOKENS[i].nome+" não declarada", self.TOKENS[i], linhas[self.TOKENS[i].linha -1 ])
                else:
                    utils.gerar_menssagem_erro("Variável "+ self.TOKENS[i].nome+" não declarada", self.TOKENS[i], linhas[self.TOKENS[i].linha -1])
        return r
    def verificar_tipo(self, identificador, dado, linha):
        if identificador.tipo_dado == "":
            return
        if identificador.tipo_dado == "VOID" and len(dado) > 0:
            utils.gerar_menssagem_erro_tipos_incompativeis(identificador, dado[0], linha[dado[0].linha-1])
            #utils.gerar_menssagem_erro("Tipos incompatíveis", dado[0], linha[dado[0].linha-1])
            return
        if len(dado) == 1:
            if identificador.tipo_dado == "FLOAT" and dado[0].tipo_dado == "INT":
                pass
            elif identificador.tipo_dado == "string" and dado[0].tipodado == "char":
                pass
            elif dado[0].tipo_dado ==  "":
                pass
            elif identificador.tipo_dado != dado[0].tipo_dado:
                utils.gerar_menssagem_erro_tipos_incompativeis(identificador, dado[0], linha[dado[0].linha-1])
            
        elif len(dado) > 1:
            if identificador.tipo_dado == "INT" or identificador.tipo_dado == "CHAR":
                for t in dado:
                    if t.token == ABRE_P.token or t.token == FECHA_P.token or t.token == VIRGULA.token:
                        continue
                    if t.tipo_dado == "INT":
                        pass
                    elif t.categoria == "math":
                        pass
                    else:
                        #print("357 ", identificador)
                        utils.gerar_menssagem_erro_tipos_incompativeis(identificador, t, linha[t.linha-1])
            elif identificador.tipo_dado == "FLOAT":
                for t in dado:
                    if t.tipo_dado != "FLOAT" and t.tipo_dado != "INT":
                        utils.gerar_menssagem_erro_tipos_incompativeis(identificador, t, linha[t.linha-1])
            elif identificador.tipo_dado == "BOOL":
                l = dado[0].linha-1
                to = dado[0]
                tres_end = Tres()
                tres_end.verificar_exp(dado)
                print_code()
                if tres_end.isBool == False:    
                    utils.gerar_menssagem_erro_tipos_incompativeis(identificador, to, linha[to.linha-1])              
                    
                    
        
        
         
        
