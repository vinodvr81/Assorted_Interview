import unittest

def user_add(x, y, z):
    return x+y+z

class TestUnitExample(unittest.TestCase):
    def test_user_add(self):
        self.assertEqual(user_add(10,20,30),60)  # add assertion here


if __name__ == '__main__':
    unittest.main()
