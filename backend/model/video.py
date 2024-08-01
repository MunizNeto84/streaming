import re
from pydantic import BaseModel, Field
from typing import Optional

class Video(BaseModel):
    categoria_id: int = Field(1, description = "ID da categoria")
    titulo: Optional[str] = Field("titulo", description = "Titulo do vídeo")
    descricao: Optional[str] = Field("decricao do video", description = "Descrição do vídeo")
    url: Optional[str] = Field("https://www.youtube.com/watch?v=string", description = "Url do vídeo")

    @staticmethod
    def get_all_videos(search=None):
        if search:
            return f"SELECT * FROM videos WHERE titulo ILIKE '%{search}%';"
        return "SELECT * FROM videos;"

    @staticmethod
    def get_videos_by_page(linhas: int, offset: int):
        return f"SELECT * FROM videos LIMIT {linhas} OFFSET {offset};"   
    
    @staticmethod
    def get_video_by_id(id):
        return f"SELECT * FROM videos WHERE videos.id = {id};"
    
    @staticmethod
    def insert_video(categoria_id, titulo, descricao, url):
        if not Video.validate_url(url):
            return f"URL must start with 'http://' or 'https://'"
        return f"INSERT INTO videos (categoria_id, titulo, descricao, url) VALUES ('{categoria_id}', '{titulo}', '{descricao}', '{url}');"
    
    @staticmethod
    def edit_video(id, categoria_id, titulo, descricao, url):
        if not Video.validate_url(url):
            return f"URL must start with 'http://' or 'https://'"
        return f"UPDATE videos SET categoria_id ='{categoria_id}', titulo = '{titulo}', descricao = '{descricao}', url = '{url}' WHERE id = {id};"   
    
    @staticmethod
    def delete_video(id):
        return f"DELETE FROM videos WHERE videos.id = {id}"
    
    def validate_url(url):
        url_regex = re.compile(
            r'^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
        )
        if not url_regex.match(url):
            raise ValueError('Invalid URL')
        return url
    
    
        
        