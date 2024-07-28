from fastapi import FastAPI
from typing import Optional

from backend.controller.video import Video, get_videos, get_videos_by_id, insert_video, edit_video, delete_video
from backend.controller.categoria import Categoria, get_categoria, get_categoria_id, insert_categoria, edit_categoria, delete_categoria

app = FastAPI()

@app.get("/video", tags=["Video"])
def get_video_endpoint(search: Optional[str] = None):
    """
    Endpoint para buscar todos os vídeos ou buscar vídeos por um termo específico.

    Parâmetros:
    - search (str, opcional): Um termo de busca para filtrar os vídeos por título.
    
    Código de Status:
    - 200 OK: Se a operação for bem-sucedida e vídeos forem encontrados.
    - 400 Bad Request: Se ocorrer um erro ao buscar os vídeos.
    """
    response = get_videos(search)
    return response

@app.get("/video/{id}", tags=["Video"])
def get_video_by_id_endpoint(id):
    """
    Endpoint para buscar video por um id específico.

    Parâmetros:
    - id (int): Uma busca para trazer o video por id.
    
    Código de Status:
    - 200 OK: Se a operação for bem-sucedida e vídeos forem encontrados.
    - 400 Bad Request: Se ocorrer um erro ao buscar os vídeos.
    - 404 Not found: Se não encontrar video.
    """
    response = get_videos_by_id(id)
    return response

@app.post("/video", tags=["Video"])
def post_insert_video_endpoint(video: Video):
    """
    Endpoint para inserir um vídeo na base de dados.

    Parâmetros:
    - categoria_id (int, opcional): Categoria do vídeo.
    - titulo (str): Título do vídeo.
    - descricao (str): Descrição do vídeo.
    - url (str): URL do vídeo.

    Código de Status:
    - 201 Created: Se o vídeo foi criado.
    - 400 Bad Request: Se ocorrer um erro ao inserir o vídeo.
    """  
    response = insert_video(video)
    return response

@app.put("/video/{id}", tags=["Video"])
def put_edit_video_endpoint(id, categoria_id, titulo, descricao, url):
    """
    Endpoint para editar um vídeo na base de dados.

    Parâmetros:
    - categoria_id (int): Categoria do vídeo.
    - titulo (str): Título do vídeo.
    - descricao (str): Descrição do vídeo.
    - url (str): URL do vídeo.

    Código de Status:
    - 201 Created: Se o vídeo foi criado.
    - 400 Bad Request: Se ocorrer um erro ao inserir o vídeo.
    """ 
    response = edit_video(id, categoria_id, titulo, descricao, url)
    return response

@app.delete("/video/{id}", tags=["Video"])
def delete_video_endpoint(id: int):
    """
    Endpoint para deletar um vídeo da base de dados.

    Parâmetros:
    - id (int): ID do vídeo a ser deletado.

    Código de Status:
    - 200 OK: Se o vídeo foi deletado com sucesso.
    - 404 Not Found: Se o vídeo não for encontrado.
    - 400 Bad Request: Se ocorrer um erro ao deletar o vídeo.
    """
    response = delete_video(id)
    return response

@app.get("/categoria", tags=["Categoria"])
def get_category_endpoint():
    """
    Endpoint para buscar todas as categorias.

    Código de Status:
    - 200 OK: Se as categorias foram buscadas com sucesso.
    - 400 Bad Request: Se ocorrer um erro ao buscar as categorias.
    """
    response = get_categoria()
    return response

@app.get("/categoria/{id}", tags=["Categoria"])
def get_category_endpoint(id):
    """
    Endpoint para buscar a categoria por id.

    Parâmetros:
    - id (int): Uma busca para trazer o video por id.

    Código de Status:
    - 200 OK: Se as categorias foram buscadas com sucesso.
    - 400 Bad Request: Se ocorrer um erro ao buscar as categorias.
    """
    response = get_categoria_id(id)
    return response

@app.post("/categoria", tags=["Categoria"])
def post_insert_categoria_endpoint(categoria: Categoria):
    """
    Endpoint para inserir uma categoria da base de dados.

    Parâmetros:
    - titulo (str): Titulo da categoria.
    - cor (str): codigo da cor da categoria.

    Código de Status:
    - 201 Create: Se o categoria foi criada com sucesso.
    - 400 Bad Request: Se ocorrer um erro ao criar o categoria.
    """
    response = insert_categoria(categoria)
    return response

@app.put("/category/{id}", tags=["Categoria"])
def edit_category_endpoint(id: int, titulo: str, cor: str):
    """
    Endpoint para editar uma categoria.

    Parâmetros:
    - id (int): Id da categoria.
    - titulo (str): Titulo da categoria.
    - cor (str): Codigo da cor da categoria.

    Código de Status:
    - 200 Create: Se o categoria foi editada com sucesso.
    - 404 Not Found: Se o categoria não for encontrado.
    - 400 Bad Request: Se ocorrer um erro ao criar o categoria.
    """
    response = edit_categoria(id, titulo, cor)
    return response

@app.delete("/category/{id}", tags=["Categoria"])
def delete_categoria_endpoint(id):
    """
    Endpoint para deletar uma categoria da base de dados.

    Parâmetros:
    - id (int): ID do categoria a ser deletada.

    Código de Status:
    - 200 OK: Se a categoria foi deletada com sucesso.
    - 404 Not Found: Se a categoria não for encontrada.
    - 400 Bad Request: Se ocorrer um erro ao deletar a categoria.
    """
    response = delete_categoria(id)
    return response
