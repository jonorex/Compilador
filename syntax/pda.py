
import sys
import os
 
current = os.path.dirname(os.path.realpath(__file__))

parent = os.path.dirname(current)
sys.path.append(parent)
 

sys.path.append('../compiladorPython')

from consts import *
from lexer import eDelimitador
from data import ABRE_P, VIRGULA

class Pda:
    def __init__(self, estadoInicial, nEstados, estadosFinais, transicoes) -> None:
        self.estadoInicial = "q0"
        self.nEstados = nEstados
        self.estadosFinais = estadosFinais
        self.pilha = []
        self.pilha = []
        self.transicoes = transicoes
        self.estadoAtual = "q0"

    def verificarTransicao(self, token, transicao):
        campo_analisado = transicao.campo_analisado
        condicao = transicao.condicao

        if transicao.palavra_chave != ABRE_P.token and transicao.palavra_chave != VIRGULA.token and len(self.pilha) > 0 and self.pilha[-1] == TOKEN_ID.token:
            self.pilha.pop()

        if(campo_analisado == TIPO and condicao == IGUAL):
            if token.tipo == transicao.palavra_chave:
                if self.mod_pilha(transicao):
                    self.estadoAtual = transicao.estado_final
                    return True
                else: return False
            else:
                return False
        elif(campo_analisado == TIPO and condicao == DIFERENTE):
            if token.tipo != transicao.palavra_chave:
                if self.mod_pilha(transicao):
                    self.estadoAtual = transicao.estado_final
                    return True
                else: return False
            else: return False
        elif(campo_analisado == TOKEN and condicao == IGUAL):
            if token.token == transicao.palavra_chave or transicao.palavra_chave == "": 
                if self.mod_pilha(transicao):
    
                    self.estadoAtual = transicao.estado_final
                    return True
                else: return False
            else: return False
        elif(campo_analisado == TOKEN and condicao == DIFERENTE):
            if token.token != transicao.palavra_chave:
                if self.mod_pilha(transicao):
                    self.estadoAtual = transicao.estado_final
                    return True
                else: return False
            else: return False
        else:
            return False
        
    def mod_pilha(self, transicao):
        if transicao.op_pilha == MANTER:
            return True
        if transicao.op_pilha == EMPILHAR:
            if eDelimitador(transicao.palavra_chave) != False:
                self.pilha.append(transicao.alteracao_pilha)
                return True
            else:
                self.pilha.append(transicao.alteracao_pilha)
                return True
        elif transicao.op_pilha == DESEMPILHAR and len(self.pilha) > 0:
            if eDelimitador(transicao.palavra_chave) != False:
                if(len(self.pilha) > 0 and self.pilha[-1] == transicao.alteracao_pilha):
                    self.pilha.pop()
                    return True
                elif transicao.alteracao_pilha == "IF" and self.pilha[-1] != "IF":
                    return True
            elif eDelimitador(transicao.palavra_chave) == False:
                if(len(self.pilha) > 0 and self.pilha[-1] == transicao.alteracao_pilha):
                    self.pilha.pop()
                    return True
            return False
        elif transicao.op_pilha == VER_TOPO:
            
            if len(transicao.alteracao_pilha) == 2:
                if len(self.pilha) >  1:
                    if(self.pilha[-1] == transicao.alteracao_pilha[-1].strip() 
                       and  self.pilha[-2] == transicao.alteracao_pilha[-2].strip()):
                        del self.pilha[-2]
                        return True
            if(len(self.pilha) >  0  and  self.pilha[-1] == transicao.alteracao_pilha):
                
                return True
            else:
                return False
        elif transicao.op_pilha == "verifica":
            for p in self.pilha:
                if p == transicao.alteracao_pilha:
                    return True
            return False
        elif transicao.op_pilha == PILHA_VAZIA:
            if len(self.pilha) == 0:
                return True
            else: return False
        elif transicao.op_pilha == VERIFICA_E_EMPILHA:
            token_verificar = transicao.alteracao_pilha[0]
            token_empilhar = transicao.alteracao_pilha[1]
            if len(self.pilha) > 0 and self.pilha[-1] == token_verificar:
                self.pilha.append(token_empilhar)
                return True
            else: return False
        elif transicao.op_pilha == VERIFICA_DESEMPILHA_EMPILHA:
            token_verificar = transicao.alteracao_pilha[0]
            token_empilhar = transicao.alteracao_pilha[1]
            if len(self.pilha) > 0 and self.pilha[-1] == token_verificar:
                self.pilha.pop()
                self.pilha.append(token_empilhar)
                return True
            else: return False
        else: return False

    def parser(self, tokenList):
        s = len(tokenList)
        self.estadoAtual = "q0"
        i = 0
        while i < s:
            v = False
            for transicao in self.transicoes:

                if transicao.estado_inicial == self.estadoAtual:
                    if self.verificarTransicao(tokenList[i], transicao) == True:
                        v = True
                        print(self.estadoAtual)
                        if transicao.consumir == True:
                            i = i-1
                        break
            if not v:
                break

            i = i+1
        
        for p in self.pilha:
            print(p)

        if v:
            while( len(self.pilha) > 0 and (self.pilha[-1] == "FUN" or self.pilha[-1] == "IF" or self.pilha[-1] == TOKEN_ID.token)):
                self.pilha.pop()
            

        if len(self.pilha) == 0 and len(self.pilha) == 0:
            for e in self.estadosFinais:
                if e == self.estadoAtual:
                    return "pertence a linguagem"
            
        
        return "Não pertence a linguagem"
