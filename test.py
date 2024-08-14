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
    
    # def test_get_id_by_tags(self):
    #     response = client.get('/image/id-by-tags/?tags=%D0%B4%D0%B5%D0%BD%D1%8C%D0%B3%D0%B8')
    #     test_data = {'tags': '{деньги}', 'id': 4316277, 'url': 'http://4316265.com'}
    #     self.assertEqual(response.json(), test_data)

    def test_ilike(self):
        response = client.get('/image/id-by-tags/?tags=программа,пингвин')
        test_data = {"tags":"{праздник,программа,пингвин}","id":4316414,"url":"http://4316402.com"}
        self.assertEqual(response.json(), test_data)


unittest.main()