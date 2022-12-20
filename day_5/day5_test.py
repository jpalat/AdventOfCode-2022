import unittest
import day5

class Test_Day5(unittest.TestCase):

    def test_day5_1(self):
        with open('example.txt') as examplefile:
            input = examplefile.readlines()
        self.assertEqual(0,0, "total")

    def test_day5_2(self):
        pass



if __name__ == '__main__':
    unittest.main()