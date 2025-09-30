class LoginError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem
    
    def __str__(self):
        return f"Login Error: {self.mensagem}"