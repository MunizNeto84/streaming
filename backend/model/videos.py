class Videos:
    def __init__(self, id, titulo, descricao, url):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.url = url

    @staticmethod
    def get_video_by_id(id):
        return F"SELECT * FROM videos WHERE videos.id = {id}"
    
    @staticmethod
    def get_all_videos():
        return "SELECT * FROM videos;"
    
    @staticmethod
    def insert_video(titulo, descricao, url):
        if not Videos.validate_url(url):
            raise ValueError('URL must start with "http://" or "https://"')
        return f"INSERT INTO videos (titulo, descricao, url) VALUES ('{titulo}', '{descricao}', '{url}');"

    @staticmethod
    def edit_video(id, titulo, descricao, url):
        if not Videos.validate_url(url):
            raise ValueError('URL must start with "http://"')
        return f"UPDATE videos SET titulo = '{titulo}', descricao = '{descricao}', url = '{url}' WHERE videos.id = {id};"   

    @staticmethod
    def delete_video(id):
        return F"DELETE FROM videos WHERE videos.id = {id}"
    
    
    def validate_url(url):
        return url.startswith("http://") or url.startswith("https://")