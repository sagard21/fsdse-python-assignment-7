from unittest import TestCase
from errors import incorrect_output, no_function_found, succeed


class TestGet_prime_numbers(TestCase):
    def test_prime_numbers(self):
        try:
            from prime_numbers import get_prime_numbers
        except ImportError:
            self.assertFalse(no_function_found("get_prime_numbers"))

        result = get_prime_numbers(10)
        try:
            self.assertEqual(2, result[0])
            self.assertEqual(3, result[1])
            self.assertEqual(5, result[2])
            self.assertEqual(7, result[3])
            self.assertTrue(succeed("Test cases passed"))
        except:
            self.assertFalse(incorrect_output("function should return array of prime numbers"))
