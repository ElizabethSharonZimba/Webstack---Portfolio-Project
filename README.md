project overview 

### `README.md`

```markdown
# Hangman Game

A simple console-based Hangman game implemented in Python. Players can guess letters to reveal a hidden word, while trying to avoid running out of attempts. This project demonstrates basic programming concepts including loops, conditionals, and file handling.

## Features

- **Core Gameplay:** Players guess letters to uncover a hidden word.
- **Dynamic Word Selection:** Words are loaded from an external text file (`words.txt`).
- **Difficulty Levels:** Choose between easy, medium, and hard difficulty levels, affecting the number of allowed incorrect guesses.
- **Add New Words:** Players can add new words to the word list during gameplay.
- **Unit Testing:** Includes a test suite to verify the functionality of the game components.

## Project Structure

```
hangman/
│
├── hangman.py            # Main game code
├── words.txt             # Text file containing everyday words
└── test_hangman.py          # Test file for unit testing
```

## Requirements

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ElizabethSharonZimba/Webstack---Portfolio-Project.git
   cd hangman
   ```

2. Ensure you have Python installed:

   ```bash
   python --version
   ```

## Running the Game

To run the game, navigate to the project directory and execute:

```bash
python hangman.py
```

## Running Tests

To run the unit tests, navigate to the project directory and execute:

```bash
python -m unittest test_base.py
```

## How to Play

1. Start the game by running `hangman.py`.
2. Choose a difficulty level (1, 2, or 3).
3. Guess letters to try to uncover the hidden word.
4. If you guess a letter correctly, it will be revealed in the word.
5. If you guess incorrectly, you lose a try.
6. The game ends when you either guess the word or run out of tries.
7. After the game, you can add new words to the list.

## Contributing
Elizabeth Sharon Zimba - Back-end and game logic
Feel free to submit issues or pull requests. Contributions are welcome!

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Acknowledgements
The classic game of Hangman, which inspired this project.
ALX for providing the learning platform for this project.