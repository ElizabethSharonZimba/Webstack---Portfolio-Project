import unittest
from unittest.mock import patch, mock_open
from hangman import load_words, fill_in_char, choose_difficulty, add_word


class TestHangmanGame(unittest.TestCase):
    
    @patch("builtins.open", new_callable=mock_open, read_data="APPLE\nBANANA\nCHERRY")
    def test_load_words(self, mock_file):
        """Test that words are loaded from a file and returned as uppercase"""
        words = load_words()
        self.assertEqual(words, ['APPLE', 'BANANA', 'CHERRY'])
        mock_file.assert_called_once_with('words.txt', 'r')

    @patch("builtins.input", side_effect=['1'])
    def test_choose_difficulty_easy(self, mock_input):
        """Test that choosing easy difficulty returns 10 tries"""
        tries = choose_difficulty()
        self.assertEqual(tries, 10)

    @patch("builtins.input", side_effect=['2'])
    def test_choose_difficulty_medium(self, mock_input):
        """Test that choosing medium difficulty returns 7 tries"""
        tries = choose_difficulty()
        self.assertEqual(tries, 7)

    @patch("builtins.input", side_effect=['3'])
    def test_choose_difficulty_hard(self, mock_input):
        """Test that choosing hard difficulty returns 5 tries"""
        tries = choose_difficulty()
        self.assertEqual(tries, 5)

    @patch("builtins.input", side_effect=['4', '2'])  # Invalid input followed by valid
    def test_choose_difficulty_invalid_then_valid(self, mock_input):
        """Test that invalid input prompts again and then accepts valid input"""
        tries = choose_difficulty()
        self.assertEqual(tries, 7)

    def test_fill_in_char_single_char(self):
        """Test filling in a single character"""
        original_word = "APPLE"
        answer_word = "_____"
        char = 'P'
        filled_word = fill_in_char(original_word, answer_word, char)
        self.assertEqual(filled_word, "_PP__")

    def test_fill_in_char_multiple_chars(self):
        """Test filling in multiple characters"""
        original_word = "BANANA"
        answer_word = "B__A_A"
        char = 'N'
        filled_word = fill_in_char(original_word, answer_word, char)
        self.assertEqual(filled_word, "B_NANA")

    @patch("builtins.open", new_callable=mock_open)
    @patch("builtins.input", side_effect=["PEAR"])
    def test_add_word(self, mock_input, mock_file):
        """Test adding a new word to the word list"""
        add_word()
        mock_file().write.assert_called_once_with("PEAR\n")
        mock_input.assert_called_once_with("Enter a new word to add: ")

if __name__ == '__main__':
    unittest.main()
