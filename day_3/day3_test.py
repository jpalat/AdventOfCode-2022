import unittest
import day3

class Test_Day3(unittest.TestCase):

    def test_day3_1(self):
        with open('example.txt') as examplefile:
            input = examplefile.readlines()
        self.assertEqual(0,0, "total")

    def test_day3_2(self):
        pass



if __name__ == '__main__':
    unittest.main()