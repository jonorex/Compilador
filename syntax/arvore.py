from data import *
from lexer import TOKENS
from consts import *
import copy

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

TOKENS_LABELS = [WHILE, FUN]


class Stm:
    def __init__(self, STM_VECTOR) -> None:
        self.cont = 0
        self.temp = 0
        self.STM_VECTOR = STM_VECTOR
    
    def implement(self):
        self.cont += 1

    def fun_separator():
        pass


    def gerar_label():
        pass

    def gerar_variavel_temporaria(self,a, op, b):
        print("t"+str(self.temp)+"="+a.nome+op.chave+b.nome)
        temp = copy.copy(TOKEN_ID)
        temp.nome = ("t"+str(self.temp))
        self.temp+=1
        return temp
    
    def verificar_parenteses(self, exp, left, right):
        i = left
        if(exp[left].token ==  ABRE_P.token):
            i  = left +1
        s = len(exp)
        #print("i: ", i)
        #print("s: ", s)
        while i < s:
            if(exp[i].token == ABRE_P.token):
                return exp[i]
            i+=1
        return False
    def verificar_exp_inteira(self, exp):
        for e in exp:
            if e.token == ABRE_P.token:
                return False
        return True
    
    def recortar_expressao(self, r):
        i = 0
        #print("len",len(self.STM_VECTOR))
        #print("linha 57 ", len(self.STM_VECTOR))
        while i < len(self.STM_VECTOR):
            if self.STM_VECTOR[i] == r:
               #print("linha 59 i = ", i)
               break
            i += 1
        #print("linha 62 i =", i)
        return self.STM_VECTOR[i+1] 
                 

    def reduzir_expressao(self, exp, left, right):
        lista_expresoes = []
        if right == 0:
            right = len(exp)
        if len(exp) == 1 and exp[0].token == (TOKEN_ID.token or TOKEN_NUMERO.token):
            print(exp[0].nome)
            return exp[0]
        #print("right",right)
        #print("size", len(exp))
        if(self.verificar_exp_inteira(exp)):
            left = 0
            right = len(exp)
        
        l = self.verificar_parenteses(exp, left, right)
        #print("linha 72 ",l)
        if l != False:
           #print("entrou aqui")
           r = self.recortar_expressao(l)
           self.reduzir_expressao(exp, l.id, r.id-self.cont)
        else:
            for op in OPERADORES:
                i = left
                #print("tamanho vetor", len(exp))
                #print("right", right)
                
                while i < len(exp):
                    #print("len",len(exp))
                    #print("right", right)
                    #print(exp[i])
                    #print("linha 109 ", right)
                    #print("linha 110 ", len(exp))
                    if op.token == exp[i].token:
                        print("--------------")
                        temp = self.gerar_variavel_temporaria(exp[i-1], exp[i], exp[i+1])
                        lista_expresoes.append(temp)
                        print("linha 89",right)
                        #print("linha 90 ", len(exp))
                        #print("linha 9 ", left)
                        #del exp[right-5]
                        #if(len(exp) > right and exp[right].token ==  FECHA_P.token):
                        #    del exp[right]
                        #    right -=1
                        #print("linha 96 ",exp[i-1])
                        if(len(exp) > left and exp[left].token == ABRE_P.token):
                            del exp[left]
                            del exp[left]
                            del exp[left]
                            del exp[left]
                            del exp[left]
                            self.cont += 5
                            right = right -5 
                            exp.insert(left, temp)
                        else:
                            del exp[i-1]
                        #print("linha 98 ",exp[i-1])
                            del exp[i-1]
                        #print("linha 98 ",exp[i-1])
                            del exp[i-1]
                            self.cont +=3
                            right-=3
                        #print("linha 98 ",exp[left])
                        
                            exp.insert(i-1, temp)
                        for e in exp:
                           print(e)
                        return self.reduzir_expressao(exp, 0, 0)
                    i = i+1
                #print("---------------")
                

class IF_stm(Stm):
    def __init__(self) -> None:
        self.condition = ""
        self.stm = ""
    
    def if_stm(self):
        e = self.reduzir_expressao(self.condition)
        


class While_stm(Stm):
    def __init__(self) -> None:
        self.condition = ""
        self.stm = ""

class Atrib_stm(Stm): 
    def __init__(self) -> None:
        self.l_value = ""
        self.r_value = ""







