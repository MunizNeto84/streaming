from fastapi import FastAPI, Response, HTTPException, status
from pydantic import BaseModel
from typing import Optional

from backend.infra.db.database import Database
from backend.model.videos import Videos
from backend.model.categoria import Categoria
import json

class Video(BaseModel):
    categoria_id: int = 1
    titulo: Optional[str] = "titulo"
    descricao: Optional[str] = "decricao do video"
    url: Optional[str] = "https://www.youtube.com/watch?v=string"

app = FastAPI()
db = Database()

@app.get("/videos")
def get_videos():
    try:
        query_object = Videos.get_all_videos()
        result = db.query(query_object)
        return {"videos": result}
    
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

@app.get("/videos/{id}")
def get_videos_by_id(id):
    try:
        query_object = Videos.get_video_by_id(id)
        result = db.query(query_object)
        
        return {"videos": result}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@app.get("/videos/")
def get_videos_search(search: str):
    try:
        query_object = Videos.get_search_videos(search)
        result = db.query(query_object)
        return {"videos": result}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))  


@app.post("/video")
def create_video(video: Video):
    try:
        query_object = Videos.insert_video(video.categoria_id, video.titulo, video.descricao, video.url)
        db.query(query_object)
        return Response(
            content=json.dumps({"message": "Video adicionado com sucesso"}),
            status_code=status.HTTP_201_CREATED,
            media_type="application/json"
        )
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@app.put("/video/{id}")
def edit_video(id: int, categoria_id: str, titulo: str, descricao: str, url: str):
    try:
        query_object = Videos.edit_video(id, categoria_id, titulo, descricao, url)
        db.query(query_object)
        return {"message": "Video atualizado"}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))    
    
@app.delete("/video/{id}")
def delete_video(id):
    try:
        query_object = Videos.video_exists(id)
        result = db.query(query_object)
        if not result[0][0]:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Video, não encontrado")

        query_object = Videos.delete_video(id)
        db.query(query_object)
        return {"message": "Video, deletado com sucesso"}
            
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))    

@app.get("/category")
def get_category():
    try:
        query_object = Categoria.get_all_category()
        result = db.query(query_object)
        return {"category": result}

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))    

@app.get("/category/{id}")
def get_category_by_id(id):
    try:
        query_object = Categoria.get_category_by_id(id)
        result = db.query(query_object)
        return {"category": result}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))  

@app.post("/category")
def create_category(titulo: str, cor: str):
    try:
        query_object = Categoria.insert_category(titulo, cor)
        db.query(query_object)
        return Response(
            content=json.dumps({"message": "Categoria criada com sucesso"}),
            status_code=status.HTTP_201_CREATED,
            media_type="application/json"
        )
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

@app.put("/category/{id}")
def edit_category(id: int, titulo: str, cor: str):
    try:
        query_object = Categoria.edit_category(id, titulo, cor)
        db.query(query_object)
        return {"message": "Categoria atualizada"}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))         

@app.delete("/category/{id}")
def delete_category(id):
    try:
        query_object = Categoria.category_exists(id)
        result = db.query(query_object)
        if not result[0][0]:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Categoria, não encontrada")

        query_object = Categoria.delete_category(id)
        db.query(query_object)
        return {"message": "Categoria, deletada com sucesso"}
            
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))  