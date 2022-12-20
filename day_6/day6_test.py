import unittest
import day6

class Test_Day6(unittest.TestCase):

    def test_day6_1(self):
        with open('example.txt') as examplefile:
            input = examplefile.readlines()
        self.assertEqual(day6.sop_finder('mjqjpqmgbljsphdztnvjfqwrcgsmlb'),7, "total")
        self.assertEqual(day6.sop_finder('bvwbjplbgvbhsrlpgdmjqwftvncz'),5, "total")
        self.assertEqual(day6.sop_finder('nppdvjthqldpwncqszvftbrmjlhg'),6, "total")
        self.assertEqual(day6.sop_finder('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'),10, "total")
        self.assertEqual(day6.sop_finder('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'),11, "total")

    def test_day6_2(self):
        self.assertEqual(day6.som_finder('mjqjpqmgbljsphdztnvjfqwrcgsmlb'),19, "total")
        self.assertEqual(day6.som_finder('bvwbjplbgvbhsrlpgdmjqwftvncz'),23, "total")
        self.assertEqual(day6.som_finder('nppdvjthqldpwncqszvftbrmjlhg'),23, "total")
        self.assertEqual(day6.som_finder('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'),29, "total")
        self.assertEqual(day6.som_finder('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'),26, "total")




if __name__ == '__main__':
    unittest.main()