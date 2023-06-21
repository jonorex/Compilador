
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)
sys.path.append(parent)
 

sys.path.append('../compiladorPython')

from consts import *
from data import ABRE_P, VIRGULA, ABRE_CHAVE, FUN, FECHA_P, IF, FECHA_CHAVE
import utils.utils as utils
STM_VECTOR = []
class Pda:
    def __init__(self, estadoInicial, nEstados, estadosFinais, transicoes) -> None:
        self.estadoInicial = estadoInicial
        self.nEstados = nEstados
        self.estadosFinais = estadosFinais
        self.pilha = []
        self.pilha = []
        self.transicoes = transicoes
        self.estadoAtual = estadoInicial
        self.error_count = 0
        self.tokenList = []
        self.linhas = []
        self.i = 0
    def verificarTransicao(self, token, transicao):
        campo_analisado = transicao.campo_analisado
        condicao = transicao.condicao

        if token.token != ABRE_P.token and token.token != VIRGULA.token and len(self.pilha) > 0 and self.pilha[-1].token == TOKEN_ID.token:
            self.pilha.pop()
        
        if token.token == VIRGULA.token and self.pilha[-1].token == TOKEN_ID.token:
            self.pilha.pop()
    

        if(campo_analisado == TIPO and condicao == IGUAL):
            if token.tipo == transicao.palavra_chave:
                if self.mod_pilha(transicao, token):
                    self.estadoAtual = transicao.estado_final
                    return True
                else: return False
            else:
                return False
        
        elif(campo_analisado == TIPO and condicao == DIFERENTE):
            if token.tipo != transicao.palavra_chave:
                if self.mod_pilha(transicao, token):
                    self.estadoAtual = transicao.estado_final
                    return True
                else: return False
            else: return False
        elif(campo_analisado == TOKEN and condicao == IGUAL):
            if token.token == transicao.palavra_chave or transicao.palavra_chave == "": 
                if self.mod_pilha(transicao, token):
                    self.estadoAtual = transicao.estado_final
                    return True
                else: return False
            else: return False
        elif(campo_analisado == TOKEN and condicao == DIFERENTE):
            if token.token != transicao.palavra_chave:
                if self.mod_pilha(transicao, token):
                    self.estadoAtual = transicao.estado_final
                    return True
                else: return False
            else: return False
        else:
            return False
        
    def mod_pilha(self, transicao, token):
        if transicao.op_pilha == MANTER:
            return True
        if transicao.op_pilha == EMPILHAR:
            self.pilha.append(token)
            return True
        elif transicao.op_pilha == DESEMPILHAR and len(self.pilha) > 0: 
            if (len(self.pilha) > 1 and self.pilha[-2].token == IF.token and token.token == FECHA_CHAVE.token):
                STM_VECTOR.append(self.pilha[-2])
                del self.pilha[-2]
            if(len(self.pilha) > 1 and self.pilha[-2].token == TOKEN_ID.token and token.token == FECHA_P.token):
                STM_VECTOR.append(self.pilha[-2])
                del self.pilha[-2]
            if(len(self.pilha) > 0 and self.pilha[-1].token == transicao.alteracao_pilha):
                STM_VECTOR.append(self.pilha[-1])
                STM_VECTOR.append(token)
                self.pilha.pop()
                return True
            elif transicao.alteracao_pilha == "IF" and self.pilha[-1].token != "IF":
                return True
            return False
        elif transicao.op_pilha == VER_TOPO:
            if len(transicao.alteracao_pilha) == 2:
                if len(self.pilha) >  1:
                    #print("linha 84 ",  )
                    if(self.pilha[-1].token == transicao.alteracao_pilha[-1].strip() 
                       and  self.pilha[-2].token == transicao.alteracao_pilha[-2].strip()):
                        #STM_VECTOR.append(self.pilha[-2])
                        #del self.pilha[-2]
                        
                        return True
            if(len(self.pilha) >  0  and  self.pilha[-1].token == transicao.alteracao_pilha):
                
                return True
            else:
                return False
        elif transicao.op_pilha == "verifica":
            for p in self.pilha:
                if p.token == transicao.alteracao_pilha:
                    #print("pilha",p)
                    return True
            return False
        elif transicao.op_pilha == PILHA_VAZIA:
            if len(self.pilha) == 0:
                return True
            else: return False
        elif transicao.op_pilha == VERIFICA_E_EMPILHA:
            token_verificar = transicao.alteracao_pilha[0]
            token_empilhar = transicao.alteracao_pilha[1]
            if len(self.pilha) > 0 and self.pilha[-1].token == token_verificar:
                self.pilha.append(token)
                return True
            else: return False
        elif transicao.op_pilha == VERIFICA_DESEMPILHA_EMPILHA:
            token_verificar = transicao.alteracao_pilha[0]
            token_empilhar = transicao.alteracao_pilha[1]
            if len(self.pilha) > 0 and self.pilha[-1].token == token_verificar:
                self.pilha.pop()
                self.pilha.append(token)
                return True
            else: return False
        else: return False


  
    def parser(self):
        s = len(self.tokenList)
        j = -1
        i = 0
        while i < s:
            v = False
            tokens_esperados = []
            for transicao in self.transicoes:
                j+=1
                if transicao.estado_inicial == self.estadoAtual:
                    tokens_esperados.append(transicao)
                    if self.verificarTransicao(self.tokenList[i], transicao) == True:
                        v = True
                        print(self.estadoAtual)
                        if transicao.consumir == True:
                            i = i-1
                        break
            if not v:
                break

            i = i+1
        #for p in self.pilha:
        #    print(p)
        if v:
            while( len(self.pilha) > 0 and (self.pilha[-1].token == "FUN" or self.pilha[-1].token == "IF" or self.pilha[-1].token == TOKEN_ID.token)):
                STM_VECTOR.append(self.pilha[-1])
                self.pilha.pop()

        else:

            #for t in tokens_esperados:
            #    self.estadoAtual = t.estado_final


            utils.gerar_menssagem_erro_sintatico(self.tokenList[i], tokens_esperados, self.linhas[self.tokenList[i].linha -1])
                   
            
        
        #print("i", s)

        if len(self.pilha) == 0 and v:
            for e in self.estadosFinais:
                if e == self.estadoAtual:
                    return v
            
        
        return False