import unittest
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):
    
    # def test_get_location_returns_expected_data(self):
    #     result = get_location("186.103.48.124")
    #     self.assertEqual(
    #         result.get("country"), "Colombia"
    #     )
        
    # def test_get_location_returns_expected_data(self):
    #     result = get_location("186.103.48.124")
    #     self.assertEqual(
    #         result.get("country"), "Colombia"
    #     )

    #Para Mockear y emular la consulta a la API.
    """
        Patch, lo que hace es crearnos una nueva variable dentro de la misma prueba.
        Le indicoq que la ruta src.api_cliente.
    """
    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName" : "Colombia",
            "countryCode" : "CO"
        }
        result = get_location("186.103.48.124")
        self.assertEqual(
            result.get("countryName"), "Colombia"
        )

        #Que este haciendo el llamado a la URL correcta. Que la URL Exista
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/186.103.48.123")
        