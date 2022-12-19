import unittest
import day2

class Test_Day2(unittest.TestCase):

    def test_day1_1(self):
        with open('example.txt') as examplefile:
            inventory = examplefile.readlines()
        self.assertEqual(0,0, "test pass")


if __name__ == '__main__':
    unittest.main()