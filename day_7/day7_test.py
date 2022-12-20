import unittest
import dayX

class Test_DayX(unittest.TestCase):

    def test_dayX_1(self):
        with open('example.txt') as examplefile:
            input = examplefile.readlines()
        self.assertEqual(0,0, "total")

    def test_dayX_2(self):
        pass



if __name__ == '__main__':
    unittest.main()