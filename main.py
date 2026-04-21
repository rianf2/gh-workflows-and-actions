import unittest

class Number:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

class TestNumber(unittest.TestCase):
    def test_get_value(self):
        number = Number(420)
        self.assertEqual(420, number.get_value())

if __name__ == '__main__':
    unittest.main()

