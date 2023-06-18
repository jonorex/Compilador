from data import *
import copy
from syntax.pda import STM_VECTOR

CONT = 0

OPERADORES = [ASTERISCO, 
              BARRA, 
              MAIS, 
              MENOS,
              AND, 
              OR, 
              MAIOR, 
              MENOR, 
              MAIOR_IGUAL, 
              MENOR_IGUAL]

class Temp():
    def __init__(self) -> None:
        self.temp_var = 0

    def increment(self):
        a = self.temp_var+1
        return  a

temp_var = Temp()

class Coor:
    def __init__(self, token, pos) -> None:
        self.token = token
        self.pos = pos





class Tres:
    def __init__(self) -> None:
        listaP = []
        self.temp = 0
        self.isBool = True

    def busca(self, exp, t):
        i = -1
        for e in exp:
            i+=1
            if e == t:
                return [e, i]
        return False

    def verificar_exp(self, exp):
        a = False
        b = False
        i = -1
        for s in STM_VECTOR:
            i += 1
            
            if s.token == ABRE_P.token:
                #print("passou aqui")
                a = self.busca(exp, s)
                b = self.busca(exp, STM_VECTOR[i+1])
                if a != False and b != False:
                    break
        if a == False:
            if len(exp) == 1:
                #print(exp[0].nome)
                if exp[0].tipo_dado != "BOOL":
                    self.isBool = False
                return exp[0]
            #print(exp[len(exp)-5])
            if len(exp) >= 2:
                if self.vericar_ultimas_posicoes(exp, len(exp)-1):
                    return self.verificar_exp(exp)
        elif (a[1]-1) >= 0 and exp[a[1]-1].token == TOKEN_ID.token:
            exp2 = exp[a[1]-1:b[1]+1]
            del exp[a[1]-1:b[1]+1]
            b = self.gerarChamadaFuncao(exp2)
            exp.insert((a[1]-1), b)
            return self.verificar_exp(exp)
        else:
            exp2 = exp[a[1]+1:b[1]]
            del exp[a[1]:b[1]+1]
            b = self.verificar_exp(exp2)
            exp.insert((a[1]), b)
            return self.verificar_exp(exp)
            
             
    def vericar_ultimas_posicoes(self, lista, topo):
        for op in OPERADORES:
            i = -1 
            for t in lista:
                i+=1
                if op.token == t.token:
                    if (lista[i-1].token == TOKEN_NUMERO.token or lista[i-1].token == TOKEN_ID.token) and (lista[i+1].token == TOKEN_NUMERO.token or lista[i+1].token == TOKEN_ID.token):
                        self.gerarTemp(lista[i-1].nome, lista[i].chave, lista[i+1].nome)
                        temp = copy.copy(TOKEN_ID)
                        temp.nome = "t"+str(temp_var.temp_var-1)
                        x = i-1 
                        
                        #self.listaP.append([lista[i-1], lista[i], lista[i+1]])
                        if (lista[i-1].tipo_dado == "INT" or lista[i-1].tipo_dado == "FLOAT")  and lista[i].categoria == "math":
                            temp.tipo_dado = "INT"
                        elif (lista[i-1].tipo_dado == "INT" or lista[i-1].tipo_dado == "FLOAT")  and lista[i].categoria == "relacional":
                            temp.tipo_dado = "BOOL"
                        elif lista[i-1].tipo_dado == "BOOL" and lista[i+1].tipo_dado == "BOOL" and lista[i].categoria == "logic":
                             temp.tipo_dado = "BOOL"
                        else:
                            self.isBool = False
                        del lista[x]
                        del lista[x]
                        del lista[x]

                        lista.insert(x, temp)
                        return True
                    else:
                        return False


    def gerar_token_temporario(self, t):
        temp = copy.copy(TOKEN_ID)
        temp.nome = "t"+str(temp_var.temp_var-1)
        temp.tipo_dado = t.tipo_dado
        return temp

    def gerarTemp(self,a, b, c):
        print("t"+str(temp_var.temp_var) +" = "+a+ " "+ b + " " + c)
        temp_var.temp_var += 1
        return "temp = "+a+ " "+ b + " " + c
    
    def gerarTempFuncao(self):
        return "t"+str(temp_var.temp_var)
    
    def gerarChamadaFuncao(self, call):
        s = len(call)-1
        params = call[2:s]

        print("params")
        print(params)

        print("call", call)
        #print("Verificar parametros")
        b = self.verificar_parametros(call) 
        print("linha 130", b)
        if b==True:
            a = self.gerar_parametros(params, call[0],"")
            return a
        else:
            c = call[b[0]:b[1]]
            print("---c----")
            print(c)
            del call[b[0]:b[1]]
            a = self.verificar_exp(c)
            call.insert(b[0], a)
            
            return self.gerarChamadaFuncao(call)
            
            
        

    def split_vetor(self, params):
        lista = []
        j = 0
        s =len(params)
        for i in range(s):
            if params[i].token == VIRGULA.token:
                lista.append(params[j:i])
                j+=1
        print("lista splitada")
        for i in lista:
            print(lista)
        print("lista splitada")
        

    def verificar_parametros(self, params):
        i =0
        j = 0
        a = 0
        s = len(params)
        sub = []

        for i in range(s):
            if params[i].token == VIRGULA.token or i==s-1:
                if j == 0:
                    a = 1
                else: a = 0
                d = i-(j+1+a)
                if d > 1:
                    return([(j+1+a),i])
                #print("linha 175 d = ",d)
                #sub.append(params[j+1+a:i]) 
                j=i
        return True

    def gerar_parametros(self, params, nome, r):
        i = 0
        #self.split_vetor(params)
        print("params")
        print(params)
        for p in params:
            if p.token != VIRGULA.token:
                print("param ", p.nome)
                i += 1
        
        
        result = "call "+ str(nome.nome) + ", "+str(i)
        if r == "":
            print(result+", t"+str(temp_var.temp_var))
            temp_var.temp_var+=1
            return self.gerar_token_temporario(nome)
        else:
            print(result+", "+r)
            

class Atribuicao(Tres):
    def __init__(self, l_value, r_value) -> None:
        super().__init__()
        self.l_value = l_value
        self.r_value = r_value

    def get_l_value(self):
        return self.l_value
    
    def get_r_value(self):
        return self.verificar_exp(self.r_value)
    
    def generate(self):
        r = self.l_value.nome + " = " + self.get_r_value().nome
        print(r)
        return r

class If_stm(Tres):
    def __init__(self, condition, stm) -> None:
        super().__init__()
        self.condition = condition
        self = stm

    

    def generate(self):
        print("if_false ("+self.condition+")"+"goto")


def e_atribuicao(tokens):
    s = len(tokens)
    j = 0
    
    for i in range(s):
        if tokens[i].token != IGUAL.token:
            j +=1
        else:
            break
    #print("j", j)
    if j == 1:
        l_value = tokens[0]
    elif j == 2:
        l_value = tokens[1]
    
    r_value = tokens[j+1:s]

    #print("l_value")
    #print(l_value)
    #print("r_value")
    #print(r_value)

    atrib = Atribuicao(l_value, r_value)

    atrib.generate()

    print(temp_var.temp_var)


def parser(tokens):
    if (e_atribuicao(tokens)):
        pass


    
        

        
        
        #s = len(lista)
        #for i in range():
        #    print("parm ",lista[i])
        

    