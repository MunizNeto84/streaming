from fastapi import FastAPI

from backend.infra.db.database import Database
from backend.model.videos import Videos


app = FastAPI()
db = Database()


@app.get("/videos")
def get_videos():
    try:
        query_object = Videos.get_all_videos()
        result = db.query(query_object)
        return {"videos": result}
    
    except Exception as e:
        return {"error": str(e)}

@app.post("/video")
def add_video(titulo: str, descricao: str, url: str):
    try:
        query_object = Videos.insert_video(titulo, descricao, url)
        db.query(query_object)
        return {"message": "Video added successfully"}
    
    except Exception as e:
        return {"error": str(e)}
 


        