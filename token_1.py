class Token:
    def __init__(self, chave, token, tipo):
        self.chave = chave
        self.token = token
        self.tipo = tipo

    def __repr__(self):
        return f"{self.token}"

    def __str__(self):
        return f"{self.token}"
    
        
    