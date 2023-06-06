
class Transicao:
    def __init__(self, estado_inicial, palavra_chave, estado_final, campo_analisado, condicao, op_pilha, alteracao_pilha, consumir ) -> None:
        self.estado_inicial = estado_inicial
        self.palavra_chave = palavra_chave
        self.estado_final = estado_final
        self.campo_analisado = campo_analisado
        self.condicao = condicao 
        self.op_pilha = op_pilha
        self.alteracao_pilha = alteracao_pilha
        self.consumir = consumir

        
    def __str__(self):
        return f"{self.estado_inicial} {self.palavra_chave} {self.estado_final} {self.campo_analisado} {self.condicao} {self.op_pilha} {self.alteracao_pilha} {self.consumir}"