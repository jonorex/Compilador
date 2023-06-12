from data import *
import copy
from syntax.pda import STM_VECTOR

OPERADORES = [AND, 
              OR, 
              MAIOR, 
              MENOR, 
              MAIOR_IGUAL, 
              MENOR_IGUAL, 
              ASTERISCO, 
              BARRA, 
              MAIS, 
              MENOS]


class Coor:
    def __init__(self, token, pos) -> None:
        self.token = token
        self.pos = pos

class Tres:
    def __init__(self) -> None:
        listaP = []
        self.temp = 0
        
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
                a = self.busca(exp, s)
                b = self.busca(exp, STM_VECTOR[i+1])
                if a and b != False:
                    break
        if a == False:
            if len(exp) == 1:
                print(exp[0].nome)
                return exp[0]
            print(exp[len(exp)-5])
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
                        temp.nome = "t"+str(self.temp-1)
                        x = i-1 
                        del lista[x]
                        del lista[x]
                        del lista[x]
                        lista.insert(x, temp)
                        return True
                    else:
                        return False

    def gerarTemp(self,a, b, c):
        print("t"+str(self.temp) +" = "+a+ " "+ b + " " + c)
        self.temp += 1
        return "temp = "+a+ " "+ b + " " + c
    
    def gerarTempFuncao(self):
        return "t"+str(self.temp)
    
    def gerarChamadaFuncao(self, call):
        s = len(call)-1
        params = call[2:s]
        self.gerar_parametros(params, call[0],"")

    def gerar_parametros(self, params, nome, r):
        i = 0
        for p in params:
            if p.token != VIRGULA.token:
                print("param ", p.nome)
                i += 1
        result = "call "+ str(nome.nome) + ", "+str(i)
        if r == "":
            print(result+", t"+str(self.temp))
            self.temp+=1
        else:
            print(result+", "+r)
            
        
        
        #s = len(lista)
        #for i in range():
        #    print("parm ",lista[i])
        

    