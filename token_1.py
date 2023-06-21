class Token:
    def __init__(self, chave, token, tipo):
        self.chave = chave
        self.token = token
        self.tipo = tipo
        self.linha = 0
        self.coluna = 0
        self.nome = ""
        self.id = 0
        self.categoria = ""
        self.escopo = "Global, "
        self.tipo_dado = ""

    def inserir_escopo(self, e):
        self.escopo.append(e)

    def __repr__(self):
        return f"{self.token}"

    def __str__(self):
        return f"<{self.id},{self.chave}, {self.token}, {self.tipo}, {self.linha}, {self.coluna}, {self.nome}, {self.categoria}, {self.escopo}, {self.tipo_dado}>"
    
        
    