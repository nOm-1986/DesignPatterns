import unittest
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):
    
    def test_get_location_returns_expected_data(self):
        result = get_location("186.103.48.124")
        self.assertEqual(
            result.get("country"), "Colombia"
        )
        
    def test_get_location_returns_expected_data(self):
        result = get_location("186.103.48.124")
        self.assertEqual(
            result.get("country"), "Colombia"
        )