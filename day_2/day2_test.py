import unittest
import day2

class Test_Day2(unittest.TestCase):

    def test_day2_1(self):
        self.assertEqual(day2.score('A Y'), 8 , "win")
        self.assertEqual(day2.score('B X'), 1 , "lose")
        self.assertEqual(day2.score('C Z'), 6 , "draw")
        with open('example.txt') as examplefile:
            inventory = examplefile.readlines()
        self.assertEqual(day2.score_total(inventory), 15, "total")


if __name__ == '__main__':
    unittest.main()