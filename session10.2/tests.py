import unittest
import prime
import numpy as np

class PrimeTests(unittest.TestCase):
    """Tests for `prime.py`."""

    def test_is_seven_prime(self):
        """Is seven prime according to the lib?"""
        self.assertTrue(prime.is_prime(7))

    def test_bigger_prime_of_twelve(self):
        self.assertEqual(prime.get_next_prime(12), 13)

    def test_bigger_prime_of_thirteen(self):
        self.assertEqual(prime.get_next_prime(13), 13)

    def test_large_int64_integer_inputs(self):
        self.assertEqual(prime.get_next_prime(np.int64(2**63 - 1)), 9223372036854775809)

if __name__ == '__main__':
    unittest.main()
