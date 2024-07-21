
class Categoria:
    def __init__(self, id, titulo, cor):
        self.id = id
        self.titulo = titulo
        self.cor = cor
    
    @staticmethod
    def get_all_category():
        return "SELECT * FROM categoria;"
    
    @staticmethod
    def get_category_by_id(id):
        return f"SELECT * FROM categoria WHERE id = {id};"

    @staticmethod
    def insert_category(titulo, cor):
        return f"INSERT INTO categoria (titulo, cor) VALUES ('{titulo}', '{cor}');"