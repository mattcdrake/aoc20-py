import unittest
import day_1

class TestSolutions(unittest.TestCase):

    def test_d1p1(self):
        self.assertEqual(day_1.p1("./input/day1.txt"), "381699")

    def test_d1p2(self):
        self.assertEqual(day_1.p2("./input/day1.txt"), "111605670")


if __name__ == "__main__":
    unittest.main()

