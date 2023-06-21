from data import *
import copy
from syntax.pda import STM_VECTOR

CONT = 0


OPERADORES = [ASTERISCO, 
              BARRA, 
              MAIS, 
              MENOS,
              MAIOR, 
              MENOR, 
              MAIOR_IGUAL, 
              MENOR_IGUAL,
              INVERSOR,
              AND, 
              OR ]

label_list = []
instruction_list = []
if_list = []
class Temp():
    def __init__(self) -> None:
        self.temp_var = 0
        self.label_var = -1

    def increment(self):
        a = self.temp_var+1
        return  a
    
    def create_label(self, nameLabel):
        self.label_var += 1
        if nameLabel != "":
            self.label_var = 0
        label_list.append(str(self.label_var) +" "+ nameLabel)
    

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

                a = self.busca(exp, s)
                b = self.busca(exp, STM_VECTOR[i+1])
                if a != False and b != False:
                    break
        if a == False:
            if len(exp) == 1:
                if exp[0].tipo_dado != "BOOL":
                    self.isBool = False
                return exp[0]
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
                if op.token == t.token and op.token != INVERSOR.token:
                    if (lista[i-1].token == TOKEN_NUMERO.token or lista[i-1].token == TOKEN_ID.token) and (lista[i+1].token == TOKEN_NUMERO.token or lista[i+1].token == TOKEN_ID.token):
                        self.gerarTemp(lista[i-1].nome, lista[i].chave, lista[i+1].nome)
                        temp = copy.copy(TOKEN_ID)
                        temp.nome = "t"+str(temp_var.temp_var-1)
                        x = i-1 
                        
                        if (lista[i-1].tipo_dado == "INT" or lista[i-1].tipo_dado == "FLOAT") and (lista[i-1].tipo_dado == "INT" or lista[i-1].tipo_dado == "FLOAT")  and lista[i].categoria == "math":
                            temp.tipo_dado = "INT"
                        elif (lista[i-1].tipo_dado == "INT" or lista[i-1].tipo_dado == "FLOAT") and (lista[i+1].tipo_dado == "INT" or lista[i+1].tipo_dado == "FLOAT")  and lista[i].categoria == "relacional":
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
                elif op.token == t.token and op.token == INVERSOR.token:
                    self.gerar_token_temp_caso_not(lista[i+1].nome)
                    temp = copy.copy(TOKEN_ID)
                    temp.nome = "t"+str(temp_var.temp_var-1)
                    if lista[i+1].tipo_dado == "BOOL" and lista[i].categoria == "logic":
                             temp.tipo_dado = "BOOL"
                    else:
                        self.isBool = False
                    del lista[i]
                    del lista[i]

                    lista.insert(i, temp)
                    return True
                
    
    def gerar_token_temp_caso_not(self, nome):
        instruction_list.append("t"+str(temp_var.temp_var)+" = !"+nome)
        temp_var.create_label("")
        temp_var.temp_var += 1

    def gerar_token_temporario(self, t):
        temp = copy.copy(TOKEN_ID)
        temp.nome = "t"+str(temp_var.temp_var-1)
        temp.tipo_dado = t.tipo_dado
        return temp

    def gerarTemp(self,a, b, c):
        instruction_list.append("t"+str(temp_var.temp_var) +" = "+a+ " "+ b + " " + c)
        temp_var.create_label("")
        temp_var.temp_var += 1
    
    def gerarTempFuncao(self):
        return "t"+str(temp_var.temp_var)
    
    def gerarChamadaFuncao(self, call):
        s = len(call)-1
        params = call[2:s]

        b = self.verificar_parametros(call) 
        if b==True:
            a = self.gerar_parametros(params, call[0],"")
            return a
        else:
            c = call[b[0]:b[1]]
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
                j=i
        return True

    def gerar_parametros(self, params, nome, r):
        i = 0
        for p in params:
            if p.token != VIRGULA.token:
                temp_var.create_label("")
                instruction_list.append("param "+ p.nome)
                i += 1
        
        
        result = "call "+ str(nome.nome) + ", "+str(i)
        if r == "":
            temp_var.create_label("")
            instruction_list.append(result+", t"+str(temp_var.temp_var))
            temp_var.temp_var+=1
            return self.gerar_token_temporario(nome)
        else:
            temp_var.create_label("")
            instruction_list.append(result+", "+r)
            

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
        temp_var.create_label("")
        instruction_list.append(self.l_value.nome + " = " + self.get_r_value().nome)

class If_stm(Tres):
    def __init__(self, if_pos, insert_pos, tokens, stm) -> None:
        super().__init__()
        self.condition = []
        self.goto_pos = 0
        self.if_pos = if_pos
        self.insert_pos = insert_pos
        self.tokens = tokens
        self.stm = stm
        self.instruction = ""
        self.correcao_goto = 1
        self.while_instruction_position = 0

    def generate_condition(self):
        i = self.if_pos
        i+=1
        while self.tokens[i].token != FECHA_P.token:
            i+=1
            self.condition.append(self.tokens[i])
        self.condition.pop()
        self.correcao_goto 
        for t in self.condition:
            if t.tipo == OP:
                self.correcao_goto+=1
        if len(self.condition) > 0:
            result = self.verificar_exp(self.condition).nome
        else: 
            result = self.condition[0]
        ins = "if_false ("+result+")"
        self.instruction = ins
        temp_var.create_label("")
        instruction_list.append(ins)
        self.while_instruction_position =len(instruction_list)
    
    def update_instruction(self):
        i = -1


        while instruction_list[i] != if_list[-1].instruction:
            i+=1

        sp =  instruction_list[i].split(" ")
        sp[-1]
        result = instruction_list[i].replace(sp[-1], str(if_list[-1].goto_pos+1))
        instruction_list[i] = result

    def generate(self):
        if self.stm == "if":
            ins = " goto "+str(self.goto_pos)
            instruction_list[self.insert_pos + 1] += ins
            self.instruction += ins
        elif self.stm == "else":
            instruction_list[self.insert_pos] += " goto "+str(self.goto_pos)
            self.update_instruction()
        elif self.stm == "else_if":
            ins = " goto "+str(self.goto_pos)
            instruction_list[self.insert_pos + self.correcao_goto] += ins
            instruction_list[self.insert_pos] += " goto "+str(self.goto_pos)
            self.instruction += ins
            self.update_instruction()
        elif self.stm == "while":
            ins = " goto "+str(self.goto_pos)
            instruction_list[self.insert_pos + 1] += ins
            instruction_list.append(" goto "+str(self.while_instruction_position-1))
            self.instruction += ins


class Exp_stm(Tres):
    def __init__(self, exp) -> None:
        super().__init__()
        result = self.verificar_exp(exp)
        ins = "return "+result.nome
        instruction_list.append(ins)
        temp_var.create_label("")

def e_atribuicao(tokens):
    s = len(tokens)
    j = 0
    
    for i in range(s):
        if tokens[i].token != IGUAL.token:
            j +=1
        else:
            break
    if j == 1:
        l_value = tokens[0]
    elif j == 2:
        l_value = tokens[1]
    
    r_value = tokens[j+1:s]

    atrib = Atribuicao(l_value, r_value)
    atrib.generate()




def clear_list():
    instruction_list.clear()
    label_list .clear()
    temp_var.temp_var = 0
    temp_var.label_var = -1

def generate(tokens):
    i = -1

    while i < len(tokens)-1:
        i += 1
        
        if tokens[i].token == FUN.token: 
            temp_var.create_label(tokens[i+1].nome)
            instruction_list.append("")
        elif tokens[i].token == IGUAL.token:
            i = generate_atrib(i, tokens)
        elif tokens[i].token == IF.token:
            intervalo = get_statment(i, tokens)
            pos = copy.copy(len(instruction_list))
            if_stm = If_stm(i, pos, tokens, "if")
            if_stm.generate_condition()
            if_stm.goto_pos = generate(tokens[intervalo[0]:intervalo[1]]) +1
            i = intervalo[1]
            if_stm.generate()
            if_list.append(if_stm)
        
        elif tokens[i].token == RETURN.token:
            i = gernerate_return(i, tokens)
        elif tokens[i].token == WHILE.token:
            intervalo = get_statment(i, tokens)
            pos = copy.copy(len(instruction_list))
            #instruction_list.append("")
            temp_var.create_label("")
            else_stm = If_stm(i, pos, tokens, "while")
            else_stm.generate_condition()
            else_stm.goto_pos = generate(tokens[intervalo[0]:intervalo[1]]) +1
            i = intervalo[1]
            else_stm.generate()
            if_list.append(else_stm)
        elif tokens[i].token == ELSE.token and tokens[i+1].token != IF.token:
            intervalo = get_statment(i, tokens)
            pos = copy.copy(len(instruction_list))
            instruction_list.append("")
            temp_var.create_label("")
            else_stm = If_stm(i, pos, tokens, "else")
            else_stm.goto_pos = generate(tokens[intervalo[0]:intervalo[1]]) +1
            i = intervalo[1]
            else_stm.generate()
        elif tokens[i].token == ELSE.token and tokens[i+1].token == IF.token:
            intervalo = get_statment(i+1, tokens)
            pos = copy.copy(len(instruction_list))
            instruction_list.append("")
            temp_var.create_label("")
            else_stm = If_stm(i+1, pos, tokens, "else_if")
            else_stm.generate_condition()
            else_stm.goto_pos = generate(tokens[intervalo[0]:intervalo[1]]) +1
            i = intervalo[1]
            else_stm.generate()
            if_list.append(else_stm)

    
    return temp_var.label_var

def gernerate_return(return_pos, tokens):
    i = return_pos
    exp = []
    while tokens[i].token != PONTO_VIRGULA.token:
        i+=1
        exp.append(tokens[i])
    
    exp.pop()
    Exp_stm(exp)
    return i


def get_statment(if_position, tokens):
    i = if_position

    while i < len(tokens):
        i+=1
        if tokens[i].token == ABRE_CHAVE.token:
            inicio = i
            abre_chave = tokens[i]
            break
    j = -1
    while j < len(STM_VECTOR):
        j+=1
        if STM_VECTOR[j] ==  abre_chave:
            break
    fim = STM_VECTOR[j+1].id

    return [inicio, fim]

def generate_atrib(token_igual_position, tokens):
    i = token_igual_position
    l_value =  tokens[i-1]
    r_value = []
    while tokens[i].token != PONTO_VIRGULA.token:
        i+= 1
        r_value.append(tokens[i])
    r_value.pop()

    atrib = Atribuicao(l_value, r_value)
    atrib.generate()
    return i
    


def print_code():
    i = -1
    while i < len(instruction_list)-1:
        i+=1
        print(label_list[i] + "  " + instruction_list[i])

