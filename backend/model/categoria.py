
class Categoria:
    def __init__(self, id, titulo, cor):
        self.id = id
        self.titulo = titulo
        self.cor = cor
    
    @staticmethod
    def insert_category(titulo, cor):
        return f"INSERT INTO categoria (titulo, cor) VALUES ('{titulo}', '{cor}');"