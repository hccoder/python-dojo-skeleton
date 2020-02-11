import unittest
from dojo import dojo

class TestStringMethods(unittest.TestCase):
    def test_dojo(self):
        self.assertEqual(dojo(), 1)

if __name__ == '__main__':
    unittest.main()
