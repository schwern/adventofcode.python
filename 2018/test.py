import unittest
from main import part_one


class TestMain(unittest.TestCase):
    def testPartOne(self):
        self.assertEqual(part_one([1, 1, 1]), 3)
        self.assertEqual(part_one([1, 1, -2]), 0)
        self.assertEqual(part_one([-1, -2, -3]), -6)


if __name__ == "__main__":
    unittest.main()
