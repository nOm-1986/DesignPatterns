import unittest

from p1.product import Product

class ProductTests(unittest.TestCase):
    def setUp(self):
        self.product = Product(1, 'Mouse', 80)
    
    def test_name_getter(self):
        self.assertEqual(self.product.name, 'Mouse')
        self.product.name = 'Hola mundo'
        self.assertEqual(self.product.name, 'Hola mundo')
    
    def test_price_positive(self):
        price = self.product.price = 100
        self.assertEqual(price, 100)
    
    def test_price_less_than_zero(self):
        with self.assertRaises(ValueError) as c:
            self.product.price = -10
        self.assertEqual(str(c.exception), 'Price can not be less than one mf...')
    
    @unittest.skip('Prueba en progreso, será modificada nuevamente...')
    def test_calculate_total_price(self):
        pass