import unittest
import day1

class Test_Day1(unittest.TestCase):

    def test_day1_1(self):
        with open('example.txt') as examplefile:
            inventory = examplefile.readlines()
        self.assertEqual(day1.assign_inventory(inventory), {1: 6000, 2: 4000, 3: 11000, 4: 24000, 5: 10000}, "test pass")
        self.assertEqual(day1.find_max({1: 6000, 2: 4000, 3: 11000, 4: 24000, 5: 10000}), (4,24000), 'max found')

if __name__ == '__main__':
    unittest.main()