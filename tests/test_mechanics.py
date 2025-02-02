import unittest
from app import create_app
from app.db import db
from app.models.mechanic import Mechanic

class TestMechanics(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            # Create test mechanic
            self.test_mechanic = Mechanic(
                name="Test Mechanic",
                email="test@mechanic.com",
                specialty="Brakes"
            )
            db.session.add(self.test_mechanic)
            db.session.commit()
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_mechanics(self):
        """Test GET /api/mechanics/"""
        response = self.client.get('/api/mechanics/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Mechanic", str(response.data))

    def test_get_mechanic(self):
        """Test GET /api/mechanics/<id>"""
        response = self.client.get('/api/mechanics/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn("test@mechanic.com", str(response.data))

    def test_create_mechanic(self):
        """Test POST /api/mechanics/"""
        data = {
            "name": "New Mechanic",
            "email": "new@mechanic.com",
            "specialty": "Engine"
        }
        response = self.client.post('/api/mechanics/', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("New Mechanic", str(response.data))

    def test_create_invalid_mechanic(self):
        """Test POST /api/mechanics/ with invalid data"""
        data = {
            "name": "Invalid Mechanic"
            # Missing required email field
        }
        response = self.client.post('/api/mechanics/', json=data)
        self.assertEqual(response.status_code, 400)

    def test_update_mechanic(self):
        """Test PUT /api/mechanics/<id>"""
        data = {"specialty": "Updated Specialty"}
        response = self.client.put('/api/mechanics/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Updated Specialty", str(response.data))

    def test_delete_mechanic(self):
        """Test DELETE /api/mechanics/<id>"""
        response = self.client.delete('/api/mechanics/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()