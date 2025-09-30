class ViewError(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        self.mensagem = mensagem
    
    def __str__(self):
        return f"Viewing Error: {self.mensagem}"