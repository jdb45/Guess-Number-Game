import unittest
from guess_the_number import Guess_The_Number


class TestGuessTheNumber(unittest.TestCase):

    # testing to make sure the check guess function is correctly displaying the right message
    def test_check_guess(self):

        self.assertEqual('guess is too low!', Guess_The_Number.check_guess(2, 4))

        self.assertEqual('guess is too high!', Guess_The_Number.check_guess(7, 2))

    # testing to make sure the random number generator is assigning a number in-between the right range
    def test_random_number(self):
        range_list = range(1, 10)
        get_random_num = Guess_The_Number.get_random_Number()
        self.assertIn(get_random_num, range_list)
