import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        # Configura el cliente de prueba de Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_saludo(self):
        # Prueba para la ruta /saludo
        response = self.app.get('/saludo?cadenadeentrada=Cristian')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hola Cristian desde la API de Python', response.data)

if __name__ == '__main__':
    unittest.main()