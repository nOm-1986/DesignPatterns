import unittest, os
from dotenv import load_dotenv 

load_dotenv()
SERVER = os.getenv("SERVER")

class AllAssertsTests(unittest.TestCase):
    
    def test_assert(self):
        self.assertEqual(10, 10)
        self.assertEqual('Hola', 'Hola')
    
    def test_assert_true_or_false(self):
        self.assertTrue(True, 1)
        self.assertFalse(False, 0)

    def test_assert_raises(self):
        with self.assertRaises(ValueError) as context:
            int('I_am_not_a_number')

    def test_assert_in(self):
        self.assertIn(10, [x for x in range(1, 11)])
        self.assertNotIn(3, [1,2])

    #Comparar dic
    def test_assert_dicts(self):
        user = {"first_name": "Fabian", "last_name": "Beltrán"}
        self.assertDictEqual(
            {"first_name": "Fabian", "last_name": "Beltrán"},
            user
        )
        self.assertSetEqual(
            {1,2,3},
            {1,2,3}
        )
    
    #Decorador skip
    @unittest.skip('Trabajo en progreso, será habilitada nuevamente.')
    def test_skip(self):
        self.assertEqual(True, 1)

    @unittest.skipIf(SERVER == "server_a", "Saltado porque no estamos en el servidor A")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(1, 2)