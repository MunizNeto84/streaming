import unittest
from fastapi.testclient import TestClient
from backend.api.main import app

class VideoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_01_post_video(self):        
        response = self.client.post("/video", json={
            "categoria_id": 1,
            "titulo": "Test vídeo",
            "descricao": "Test descrição",
            "url": "https://www.youtube.com/watch?v=test"
        })
        self.assertEqual(response.status_code, 201)

    def get_first_video_id(self):
        response = self.client.get("/video")
        videos = response.json()["videos"]
        if videos:
            return videos[0]["id"]
        else:
            return Exception("Nenhum vídeo encontrado no banco de dados")    

    def test_02_get_video_by_id(self):
        id = self.get_first_video_id()
        response = self.client.get(f"/video/{id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["video"]["id"], id)

    def test_03_put_video(self):
        id = self.get_first_video_id()
        response = self.client.put(f"/video/{id}", json={
            "id": id,
            "titulo": "Test vídeo editado",
            "descricao": "Test descrição editada",
            "url": "https://www.youtube.com/watch?v=editado",
            "categoria_id": 1,
        })
        self.assertEqual(response.status_code, 200)

    def test_04_delete_video(self):
        id = self.get_first_video_id()
        response = self.client.delete(f"/video/{id}")
        self.assertEqual(response.status_code, 200)
            

if __name__ == "__main__":
    unittest.main()