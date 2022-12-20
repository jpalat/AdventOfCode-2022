import unittest
import day3

class Test_Day3(unittest.TestCase):

    def test_day3_1(self):
        with open('example.txt') as examplefile:
            input = examplefile.readlines()
        self.assertEqual(day3.check_compartments('vJrwpWtwJgWrhcsFMMfFFhFp'),('vJrwpWtwJgWr','hcsFMMfFFhFp') , "l & r")
        self.assertEqual(day3.check_compartments('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'),('jqHRNqRjqzjGDLGL','rsFMfFZSrLrFZsSL') , "l & r")
        self.assertEqual(day3.check_compartments('PmmdzqPrVvPwwTWBwg'),('PmmdzqPrV','vPwwTWBwg') , "l & r")

        self.assertEqual(day3.compare_compartments(day3.check_compartments('vJrwpWtwJgWrhcsFMMfFFhFp')), 'p' , "l & r")
        self.assertEqual(day3.compare_compartments(day3.check_compartments('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL')), 'L' , "l & r")
        self.assertEqual(day3.compare_compartments(day3.check_compartments('PmmdzqPrVvPwwTWBwg')), 'P' , "l & r")
        self.assertEqual(day3.compare_compartments(day3.check_compartments('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn')), 'v' , "l & r")
        self.assertEqual(day3.compare_compartments(day3.check_compartments('ttgJtRGJQctTZtZT')), 't' , "l & r")
        self.assertEqual(day3.compare_compartments(day3.check_compartments('CrZsJsPPZsGzwwsLwLmpwMDw')), 's' , "l & r")

        self.assertEqual(day3.score('p'), 16,'')
        self.assertEqual(day3.score('L'), 38,'')
        self.assertEqual(day3.score('P'), 42,'')
        self.assertEqual(day3.score('v'), 22,'')
        self.assertEqual(day3.score('t'), 20,'')
        self.assertEqual(day3.score('s'), 19,'')
    def test_day3_2(self):
        with open('example.txt') as examplefile:
            input = examplefile.readlines()
        self.assertEqual(day3.find_badges(input), ['r', 'Z'], '')
        self.assertEqual(day3.badge_total(input), 70, '')


if __name__ == '__main__':
    unittest.main()