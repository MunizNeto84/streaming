from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

from backend.infra.db.database import Database
from backend.model.video import Video as VideoModel

db = Database()

def get_videos(search: str):
    try:
        query_object = VideoModel.get_all_videos(search)
        results = db.query(query_object)
        if not results:
            return JSONResponse(content={"videos": []}, status_code=200)
        
        videos = [
            {
                "id": result[0],
                "titulo": result[1],
                "descricao": result[2],
                "url": result[3],
                "categoria_id": result[4]
            } for result in results
        ]
        return JSONResponse(content={"videos": videos}, status_code=200)

  
    except Exception as e:
        JSONResponse(content={"Error": str(e)}, status_code=400)

def get_videos_by_id(id):
    try:
        query_object = VideoModel.get_video_by_id(id)
        result = db.query(query_object)
        if not result:
            return JSONResponse(content={"message": "Video não encontrado."}, status_code=404)
        video = {
                "id": result[0][0],
                "titulo": result[0][1],
                "descricao": result[0][2],
                "url": result[0][3],
                "categoria_id": result[0][4]
            }
        
        return JSONResponse(content={"video": video}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"Error": str(e)}, status_code=400) 
    
def insert_video(video: VideoModel):
    try:
        query_object = VideoModel.insert_video(video.categoria_id, video.titulo, video.descricao, video.url)
        db.query(query_object)
        video_created = {
            "titulo": video.titulo,
            "descricao": video.descricao,
            "url": video.url,
            "categoria_id": video.categoria_id
        }
        return JSONResponse(content={
            "message": "Video, criado com sucesso.",
            "video": video_created
            }, status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

def edit_video(id, categoria_id, titulo, descricao, url):
    try:
        query_object = VideoModel.get_video_by_id(id)
        result = db.query(query_object)
        if not result or not result[0]:
            return JSONResponse(content={"message": "Video não encontrado."}, status_code=404)

        query_object = VideoModel.edit_video(id, categoria_id, titulo, descricao, url)
        db.query(query_object)
        video_edited = {
            "id": id,
            "titulo": titulo,
            "descricao": descricao,
            "url": url,
            "categoria_id": categoria_id
        }
        return JSONResponse(content={
            "message": "Video, editado com sucesso.",
            "video": video_edited
            }, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)    

def delete_video(id: int):
    try:
        query_object = VideoModel.get_video_by_id(id)
        result = db.query(query_object)
        if not result:
            return JSONResponse(content={"message": "Video não encontrado."}, status_code=404)
        
        video = {
            "id": result[0][0],
            "titulo": result[0][1],
            "descricao": result[0][2],
            "url": result[0][3],
            "categoria_id": result[0][4]
        }

        query_object = VideoModel.delete_video(id)
        db.query(query_object)

        return JSONResponse(content={
            "message": "Video deletado com sucesso.",
            "video": video
        }, status_code=200)
    
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)