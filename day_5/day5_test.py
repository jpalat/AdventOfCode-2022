import unittest
import day_5

class Test_Day5(unittest.TestCase):

    def test_day5_1(self):
        with open('example.txt') as examplefile:
            input = examplefile.readlines()
        self.assertEqual(day_5.init_crates(input) ,{0: [], 5: ['M', 'C', 'D'], 1: ['Z', 'N'], 9: ['P']}, "total")
        self.assertEqual(day_5.manage_stacks(input) ,{0: [], 5: ['M'], 1: ['C'], 9: ['P', 'D', 'N', 'Z']}, "total")

    def test_day5_2(self):
        pass



if __name__ == '__main__':
    unittest.main()