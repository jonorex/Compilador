class Token:
    def __init__(self, chave, token, tipo):
        self.chave = chave
        self.token = token
        self.tipo = tipo
        self.linha = ""
        self.coluna = 0

    def __repr__(self):
        return f"{self.token}"

    def __str__(self):
        return f"{self.chave} {self.token} {self.tipo} {self.linha} {self.coluna}"
    
        
    