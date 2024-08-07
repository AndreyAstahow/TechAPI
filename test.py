import unittest

from fastapi.testclient import TestClient
from image.image_service import ImageService
from main import app


client = TestClient(app)

class TestClass(unittest.TestCase):  
    def test_get(self):
        response = client.get('/image/?id=1')
        test = {
            "tags": "s",
            "id": 1,
            "url": "h"
            }
        self.assertEqual(response.json(), test)
    
    def test_get_id_by_tags(self):
        response = client.get('/image/id-by-tags/?tags=%D0%B4%D0%B5%D0%BD%D1%8C%D0%B3%D0%B8')
        test_data = 9
        self.assertEqual(response.json(), test_data)


unittest.main()