from fastapi import FastAPI, Response, HTTPException, status
from backend.infra.db.database import Database
from backend.model.videos import Videos
from backend.model.categoria import Categoria
import json

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
def get_videos(id):
    try:
        query_object = Videos.get_video_by_id(id)
        result = db.query(query_object)
        
        return {"videos": result}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@app.post("/video")
def create_video(titulo: str, descricao: str, url: str):
    try:
        query_object = Videos.insert_video(titulo, descricao, url)
        db.query(query_object)
        return Response(
            content=json.dumps({"message": "Video added successfully"}),
            status_code=status.HTTP_201_CREATED,
            media_type="application/json"
        )
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@app.put("/video/{id}")
def edit_video(id: int, titulo: str, descricao: str, url: str):
    try:
        query_object = Videos.edit_video(id, titulo, descricao, url)
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
 


@app.post("/category")
def create_video(titulo: str, cor: str):
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