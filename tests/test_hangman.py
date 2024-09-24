import unittest
from unittest.mock import patch, mock_open
from hangman import load_words, fill_in_char, choose_difficulty, add_word

class TestHangmanGame(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data="APPLE\nBANANA\nCHERRY")
    def test_load_words(self, mock_file):
        """Test that words are loaded from a file and returned as uppercase.

        This test mocks the 'open' function to simulate reading from 'words.txt'
        with a predefined set of words. It checks if 'load_words' correctly
        returns these words in uppercase and verifies that 'open' was called
        with the correct file name and mode.

        Args:
            mock_file (MagicMock): Mock object for the 'open' function.
        """
        words = load_words()
        self.assertEqual(words, ['APPLE', 'BANANA', 'CHERRY'])
        mock_file.assert_called_once_with('words.txt', 'r')

    @patch("builtins.input", side_effect=['1'])
    def test_choose_difficulty_easy(self, mock_input):
        """Test that choosing easy difficulty returns 10 tries.

        This test mocks the 'input' function to simulate user input for selecting
        the easy difficulty level. It verifies that 'choose_difficulty' returns
        the correct number of tries (10) for the easy level.

        Args:
            mock_input (MagicMock): Mock object for the 'input' function.
        """
        tries = choose_difficulty()
        self.assertEqual(tries, 6)

    @patch("builtins.input", side_effect=['2'])
    def test_choose_difficulty_medium(self, mock_input):
        """Test that choosing medium difficulty returns 7 tries.

        This test mocks the 'input' function to simulate user input for selecting
        the medium difficulty level. It verifies that 'choose_difficulty' returns
        the correct number of tries (7) for the medium level.

        Args:
            mock_input (MagicMock): Mock object for the 'input' function.
        """
        tries = choose_difficulty()
        self.assertEqual(tries, 4)

    @patch("builtins.input", side_effect=['3'])
    def test_choose_difficulty_hard(self, mock_input):
        """Test that choosing hard difficulty returns 5 tries.

        This test mocks the 'input' function to simulate user input for selecting
        the hard difficulty level. It verifies that 'choose_difficulty' returns
        the correct number of tries (5) for the hard level.

        Args:
            mock_input (MagicMock): Mock object for the 'input' function.
        """
        tries = choose_difficulty()
        self.assertEqual(tries, 3)

    @patch("builtins.input", side_effect=['4', '2'])  # Invalid input followed by valid
    def test_choose_difficulty_invalid_then_valid(self, mock_input):
        """Test that invalid input prompts again and then accepts valid input.

        This test mocks the 'input' function to simulate invalid input followed
        by valid input. It verifies that 'choose_difficulty' prompts for a valid
        input when the initial input is invalid and returns the correct number
        of tries (7) for the medium level.

        Args:
            mock_input (MagicMock): Mock object for the 'input' function.
        """
        tries = choose_difficulty()
        self.assertEqual(tries, 4)

    def test_fill_in_char_single_char(self):
        """Test filling in a single character.

        This test checks the behavior of 'fill_in_char' when a single character
        is provided. It verifies that the guessed character is correctly filled
        into the answer word.

        """
        original_word = "APPLE"
        answer_word = "_____"
        char = 'P'
        filled_word = fill_in_char(original_word, answer_word, char)
        self.assertEqual(filled_word, "_PP__")

    def test_fill_in_char_multiple_chars(self):
        """Test filling in multiple characters.

        This test checks the behavior of 'fill_in_char' when a character that
        appears multiple times in the original word is provided. It verifies that
        all occurrences of the guessed character are correctly filled into the
        answer word.

        """
        original_word = "BANANA"
        answer_word = "B__A_A"
        char = 'N'
        filled_word = fill_in_char(original_word, answer_word, char)
        self.assertEqual(filled_word, "B_NANA")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["PEAR"])
    def test_add_word(self, mock_input, mock_file):
        """Test adding a new word to the word list.

        This test mocks both the 'input' function and the 'open' function to
        simulate adding a new word to 'words.txt'. It verifies that the word
        is correctly appended to the file and that the 'input' function was
        called to prompt for the new word.

        Args:
            mock_input (MagicMock): Mock object for the 'input' function.
            mock_file (MagicMock): Mock object for the 'open' function.
        """
        add_word()
        mock_file().write.assert_called_once_with("PEAR\n")
        mock_input.assert_called_once_with("Enter a new word to add: ")

if __name__ == '__main__':
    unittest.main()
