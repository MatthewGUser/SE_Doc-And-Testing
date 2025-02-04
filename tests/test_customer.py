from tests import BaseTestCase

class TestCustomerAPI(BaseTestCase):
    def test_get_customers(self):
        response = self.client.get('/customers')
        self.assertEqual(response.status_code, 200)
        
    def test_create_customer(self):
        data = {
            "first_name": "Test",
            "last_name": "Customer",
            "email": "test@customer.com",
            "phone": "1234567890"
        }
        response = self.client.post('/customers', json=data)
        self.assertEqual(response.status_code, 201)
        
    def test_get_customer(self):
        data = {
            "first_name": "Test",
            "last_name": "Customer",
            "email": "test@customer.com",
            "phone": "1234567890"
        }
        self.client.post('/customers', json=data)
        response = self.client.get('/customers/1')
        self.assertEqual(response.status_code, 200)

    def test_update_customer(self):
        # Create test customer
        data = {
            "first_name": "Test",
            "last_name": "Customer",
            "email": "test@customer.com",
            "phone": "1234567890"
        }
        self.client.post('/customers', json=data)
        
        # Update customer
        update_data = {"first_name": "Updated"}
        response = self.client.put('/customers/1', json=update_data)
        self.assertEqual(response.status_code, 200)
        
    def test_delete_customer(self):
        # Create test customer
        data = {
            "first_name": "Test",
            "last_name": "Customer",
            "email": "test@customer.com",
            "phone": "1234567890"
        }
        self.client.post('/customers', json=data)
        
        response = self.client.delete('/customers/1')
        self.assertEqual(response.status_code, 204)