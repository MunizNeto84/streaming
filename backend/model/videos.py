class Videos:
    def __init__(self, id, titulo, descricao, url):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.url = url

    @staticmethod
    def get_all_videos():
        return "SELECT * FROM videos;"
    
    @staticmethod
    def insert_video(titulo, descricao, url):
        return f"INSERT INTO videos (titulo, descricao, url) VALUES ('{titulo}', '{descricao}', '{url}');"    