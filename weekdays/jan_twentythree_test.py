import unittest
import jan_twenty_three

class test_string_finder(unittest.TestCase):

	def test_check_array(self):
		self.assertEqual(jan_twenty_three.check_array(["FOO", "BAR", "THUD"], ["THUD", "BAR", "FOO"]), "True")
		self.assertEqual(jan_twenty_three.check_array(["FOO", "BAR", "THUD", "CAT"], ["THUD", "BAR", "FOO"]), "False")
		self.assertEqual(jan_twenty_three.check_array(["FOO"], ["FOO", "FOO"]), "False")

	def test_check_array_dict(self):
		self.assertEqual(jan_twenty_three.check_array_dict(["FOO", "BAR", "THUD"], ["THUD", "BAR", "FOO"]), "True")
		self.assertEqual(jan_twenty_three.check_array_dict(["FOO", "BAR", "THUD", "CAT"], ["THUD", "BAR", "FOO"]), "False")
		self.assertEqual(jan_twenty_three.check_array_dict(["FOO"], ["FOO", "FOO"]), "False")


if __name__ == "__main__":
	unittest.main()
