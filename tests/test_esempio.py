import unittest
import sys
import os

# Aggiunge 'src' al path per permettere gli import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from esempio import somma

class TestSomma(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(somma(2, 3), 5)

if __name__ == '__main__':
    unittest.main()
