import unittest

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