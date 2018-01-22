import unittest
import jan_twenty_two_code

class test_string_finder(unittest.TestCase):

	def test_list_string_diff(self):
		self.assertEqual(jan_twenty_two_code.mxdiflg(["hoqq"], ["cccoir"]), 2)
		self.assertEqual(jan_twenty_two_code.mxdiflg(["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"],["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]),13)

if __name__ == '__main__':
	unittest.main()