import unittest
import prime_number_list

class TestPrimeNumbers(unittest.TestCase):

	# Check if it returns a list of prime numbers between 0 & 10
	def test_return_prime_10(self):
		self.assertEqual(prime_number_list.prime_number_list(10), [2, 3, 5, 7])

	# Check if it returns a list of prime numbers between 0 & 100
	def test_return_prime_100(self):
		self.assertEqual(prime_number_list.prime_number_list(100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

	# Check if it returns a list of prime numbers between 0 & 200
	def test_return_prime_200(self):
		self.assertEqual(prime_number_list.prime_number_list(200), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])

	# Check if it returns a list of prime numbers between 0 & 239
	def test_return_prime_300(self):
		self.assertEqual(prime_number_list.prime_number_list(239), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239])
	# Check if it returns a list of prime numbers between 0 & 500
	def test_return_prime_500(self):
		self.assertEqual(prime_number_list.prime_number_list(500), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499])

	# Check if it returns a list of prime numbers between 0 & 1000
	def test_return_prime_1000(self):
		self.assertEqual(prime_number_list.prime_number_list(1000), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997])

	# check if argument is zero
	def test_if_zero(self):
		self.assertEqual(prime_number_list.prime_number_list(0), "Input Variable cannot be zero")

	# check if arguments passed is not an integer
	def test_if_wrong_type(self):
		self.assertEqual(prime_number_list.prime_number_list("20"), "Input Variable should be Integer")

	# check if parameter is not less than zero / is a positve integer
	def test_if_positive_integer(self):
		self.assertEqual(prime_number_list.prime_number_list(-5), "Input Variable should be a positive integer")

	# Check if parameter is greater than 1
	def test_if_greater_than_one(self):
		self.assertEqual(prime_number_list.prime_number_list(1), "Input Variable should be greater than one")
	