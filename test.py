import unittest
import day_1
import day_2

class TestSolutions(unittest.TestCase):

    def test_d1_p_1(self):
        self.assertEqual(day_1.p_1("./input/day1.txt"), "381699")

    def test_d1_p_2(self):
        self.assertEqual(day_1.p_2("./input/day1.txt"), "111605670")

    def test_d2_p_1(self):
        self.assertEqual(day_2.p_1("./input/day2.txt"), "447")

    def test_d2_p_2(self):
        self.assertEqual(day_2.p_2("./input/day2.txt"), "249")


if __name__ == "__main__":
    unittest.main()

