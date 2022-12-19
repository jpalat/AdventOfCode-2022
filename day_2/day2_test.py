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

    def test_day2_2(self):
        print("Test 2")
        self.assertEqual(day2.score_new('A Y'), 4 , "draw - rock")
        self.assertEqual(day2.score_new('B X'), 1 , "lose - rock")
        self.assertEqual(day2.score_new('C Z'), 7 , "win - Rock")
        with open('example.txt') as examplefile:
            inventory = examplefile.readlines()
        self.assertEqual(day2.score_total(inventory, True), 12, "total")



if __name__ == '__main__':
    unittest.main()