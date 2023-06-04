import unittest, time

from app import app
from elastic import query_index_by_text

class Test1(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_true_delete(self):
        response = self.app.delete("/delete/?id=42").data.decode()
        assert response == 'True'
    
    def test_delete_invalid_id(self):
        response = self.app.delete("/delete/?id=6666").data.decode()
        assert response == 'ID not found'

class Test2(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_false_delete(self):
        response = self.app.delete("/delete/?id=42").data.decode()
        assert response == 'ID not found'
    
    def test_get_ids(self):
        response = query_index_by_text('docs', 'аааа')
        assert response == [130, 131, 293, 385]

class Test3(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_search_by_text(self):
        response = self.app.get("/search/?text=боевой таз")
        assert response.status_code == 5
        
class Test4(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_id_after_delete(self):
        self.app.delete("/delete/?id=384")
        time.sleep(2)
        response = query_index_by_text('docs', 'ааааа')
        assert response == [385]

if __name__ == '__main__':
    unittest.main()
        
