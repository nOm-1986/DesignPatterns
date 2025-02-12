import unittest

from p1.product import Product

class ProductTests(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, 'Mouse', 80)
    
    def test_name_getter(self):
        self.assertEqual(self.product.name, 'Mouse')
        self.product.name = 'Hola mundo'
        self.assertEqual(self.product.name, 'Hola mundo')