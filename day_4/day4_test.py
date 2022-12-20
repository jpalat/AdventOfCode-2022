import unittest
import day4

class Test_Day4(unittest.TestCase):

    def test_day4_1(self):
        with open('example.txt') as examplefile:
            input = examplefile.readlines()
        self.assertEqual(day4.range_check('2-4,6-8'),False, "total")
        self.assertEqual(day4.range_check('6-6,4-6'),True, "total")
        self.assertEqual(day4.range_check('2-8,3-7'),True, "total")

    def test_day4_2(self):
        self.assertEqual(day4.range_check2('5-7,7-9'),True, "total")
        self.assertEqual(day4.range_check2('2-8,3-7'),True, "total")
        self.assertEqual(day4.range_check2('6-6,4-6'),True, "total")
        self.assertEqual(day4.range_check2('2-6,4-8'),True, "total")


if __name__ == '__main__':
    unittest.main()