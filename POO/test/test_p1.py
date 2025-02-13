import unittest
from p1.person import Person

class PersonTests(unittest.TestCase):
    def setUp(self):
        self.person = Person('Fabian', 38)

    def test_greeting_string_name(self):
        self.assertEqual(self.person.greeting(), 'Hello Fabian')

    def test_is_of_legal_age(self):
        self.assertTrue(self.person.is_of_legal_age(), 'You do not have enough age')

    def test_age(self):
        self.assertEqual(self.person.show_age(),38)

    def test_name(self):
        self.assertEqual(self.person.name, 'Fabian')
        new_name = self.person.name = 'Majo'
        self.assertEqual(new_name,  'Majo')