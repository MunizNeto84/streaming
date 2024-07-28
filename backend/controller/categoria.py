from fastapi.responses import JSONResponse
from pydantic import BaseModel

from backend.infra.db.database import Database
from backend.model.categoria import Categoria as CategoriaModel

db = Database()

def get_categoria():
    try:
        query_object = CategoriaModel.get_all_category()
        results = db.query(query_object)
        if not results:
            return JSONResponse(content={"categorias": []}, status_code=200)
        
        categorias = [
            {
                "id": result[0],
                "titulo": result[1],
                "cor": result[2],
            } for result in results
        ]
        return JSONResponse(content={"categoria": categorias}, status_code=200)
  
    except Exception as e:
        JSONResponse(content={"Error": str(e)}, status_code=400)

def get_categoria_id(id):
    try:
        query_object = CategoriaModel.get_category_by_id(id)
        result = db.query(query_object)
        if not result:
            return JSONResponse(content={"message": "Categoria, não encontrada."}, status_code=404)
        
        categorias = [
            {
                "id": result[0][0],
                "titulo": result[0][1],
                "cor": result[0][2]
            }
        ]

        return JSONResponse(content={"Categoria": categorias}, status_code=200)
    
    except Exception as e:
        JSONResponse(content={"Error": str(e)}, status_code=400)

def insert_categoria(categoria: CategoriaModel):
    try:
        query_object = CategoriaModel.insert_category(categoria.titulo, categoria.cor)
        db.query(query_object)

        categoria_created = {
            "titulo": categoria.titulo,
            "cor": categoria.cor
        }

        return JSONResponse(
            content={
            "message": "Categoria, criada com sucesso.",
            "video": categoria_created
            }, status_code=201
        )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

def edit_categoria(id, titulo, cor):
    try:
        query_object = CategoriaModel.get_category_by_id(id)
        result = db.query(query_object)
        if not result:
            return JSONResponse(content={"message": "Categoria, não encontrada."}, status_code=404)
        
        categoria_edited = {
            "id": id,
            "titulo": titulo,
            "cor": cor
        }

        query_object = CategoriaModel.edit_category(id, titulo, cor)
        db.query(query_object)

        return JSONResponse(
            content={
            "message": "Categoria, editada com sucesso.",
            "video": categoria_edited
            }, status_code=200
        )

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

def delete_categoria(id):
    try:
        query_object = CategoriaModel.get_category_by_id(id)
        result = db.query(query_object)
        if not result:
            return JSONResponse(content={"message": "Categoria, não encontrada."}, status_code=404)
        
        categoria = {
            "id": result[0][0],
            "titulo": result[0][1],
            "cor": result[0][2]
        }

        query_object = CategoriaModel.delete_category(id)
        db.query(query_object)

        return JSONResponse(
            content={
            "message": "Categoria, deletada com sucesso.",
            "video": categoria
            }, status_code=200
        )
        
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)    
    
def exibir_video_by_categoria(id):
    try:    
        query_object = CategoriaModel.get_category_by_id(id)
        result = db.query(query_object)
        if not result:
            return JSONResponse(content={"message": "Categoria, não encontrada."}, status_code=404)
        
        query_object = CategoriaModel.exibir_video_by_category(id)
        results = db.query(query_object)

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
        return JSONResponse(content={"error": str(e)}, status_code=400)    
