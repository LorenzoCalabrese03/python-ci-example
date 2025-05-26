import unittest
from src.esempio import somma

class TestSomma(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(somma(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
