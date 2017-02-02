import unittest
from unittest.mock import patch, call
from guess_the_number import Guess_The_Number


class TestGuessTheNumber(unittest.TestCase):


    @patch('Guess_The_Number.get_random_Number', return_value=4)
    @patch('Guess_The_Number.get_user_input', side_effect=[3, 10, 4])
    @patch('builtins.print')

    def test_play_game(self, mock_print, mock_input):
        Guess_The_Number.main()

        expected_calls = [call(3), call(10)]
        self.assertEqual(expected_calls, mock_input.call_args_list)


if __name__ == '__main__':
    unittest.main()
