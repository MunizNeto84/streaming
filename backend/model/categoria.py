
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
    
    @staticmethod
    def edit_category(id, titulo, cor):
        return f"UPDATE categoria SET titulo = '{titulo}', cor = '{cor}' WHERE id = {id};" 

    @staticmethod
    def delete_category(id):
        return f"DELETE FROM categoria WHERE id = {id}"
    
    @staticmethod
    def exibir_video_by_category(id):
        return f"SELECT * FROM videos WHERE categoria_id = {id}"