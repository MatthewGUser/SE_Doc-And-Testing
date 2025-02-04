from tests import BaseTestCase

class TestMechanicAPI(BaseTestCase):
    def test_get_mechanics(self):
        response = self.client.get('/mechanics')
        self.assertEqual(response.status_code, 200)
        
    def test_create_mechanic(self):
        data = {
            "name": "Test Mechanic",
            "email": "test@mechanic.com",
            "specialty": "Test Specialty"
        }
        response = self.client.post('/mechanics', json=data)
        self.assertEqual(response.status_code, 201)
        
    def test_get_mechanic(self):
        data = {"name": "Test", "email": "test@test.com", "specialty": "Testing"}
        self.client.post('/mechanics', json=data)
        response = self.client.get('/mechanics/1')
        self.assertEqual(response.status_code, 200)
        
    def test_update_mechanic(self):
        data = {"name": "Test", "email": "test@test.com", "specialty": "Testing"}
        self.client.post('/mechanics', json=data)
        update_data = {"name": "Updated Name"}
        response = self.client.put('/mechanics/1', json=update_data)
        self.assertEqual(response.status_code, 200)
        
    def test_delete_mechanic(self):
        data = {"name": "Test", "email": "test@test.com", "specialty": "Testing"}
        self.client.post('/mechanics', json=data)
        response = self.client.delete('/mechanics/1')
        self.assertEqual(response.status_code, 204)