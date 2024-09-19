# Hangman Game API

## Introduction
This API provides functionality to play the Hangman game. It allows users to start a new game, submit guesses, retrieve the current game status, and end the game. This documentation provides a comprehensive guide on how to interact with the API.

## Base URL

http://localhost:5000/api/v1

markdown


## Endpoints

### 1. Start a New Game
- **Method:** `POST`
- **URL:** `/game/start`
- **Description:** Starts a new game of Hangman.
- **Request Body:**
  ```json
  {
    "difficulty": "easy" 
  }

    Response Format:
        Success (201 Created):

        json

{
  "game_id": 1,
  "word": "apple",
  "remaining_tries": 10,
  "current_status": "_____"
}

Error (400 Bad Request):

json

        {
          "error": "Invalid difficulty level"
        }

2. Submit a Guess

    Method: POST
    URL: /game/{game_id}/guess
    Description: Submits a letter guess for the current game.
    Request Body:

    json

{
  "letter": "a"
}

Response Format:

    Success (200 OK):

    json

{
  "current_status": "_pp__",
  "remaining_tries": 9,
  "message": "Correct guess!"  // or "Wrong guess!"
}

Error (400 Bad Request):

json

        {
          "error": "Invalid guess"
        }

3. Get Game Status

    Method: GET
    URL: /game/{game_id}
    Description: Retrieves the current status of the game.
    Response Format:
        Success (200 OK):

        json

{
  "game_id": 1,
  "current_status": "_pp__",
  "remaining_tries": 9,
  "word": "apple"
}

Error (404 Not Found):

json

        {
          "error": "Game not found"
        }

4. End Game

    Method: DELETE
    URL: /game/{game_id}
    Description: Ends the game and reveals the word.
    Response Format:
        Success (204 No Content):
            No content returned.
        Error (404 Not Found):

        json

        {
          "error": "Game not found"
        }

Error Handling
Code	Message
400	Bad Request
404	Not Found
500	Internal Server Error
Rate Limiting

    Each user can make up to 100 requests per hour.

Installation

    Clone the repository:

    bash

git clone https://github.com/ElizabethSharonZimba/Webstack---Portfolio-Project.git
cd Webstack---Portfolio-Project

Ensure you have Python installed:

bash

python --version

Install dependencies:

bash

pip install -r requirements.txt

Run the application:

bash
   python hangman.py
   python hangman_api.py

Running Tests

To run the unit tests, navigate to the project directory and execute:

bash

python -m unittest test_hangman.py

Project Overview
Hangman Game

A simple console-based Hangman game implemented in Python. Players can guess letters to reveal a hidden word, while trying to avoid running out of attempts. This project demonstrates basic programming concepts including loops, conditionals, and file handling.
Features

    Core Gameplay: Players guess letters to uncover a hidden word.
    Dynamic Word Selection: Words are loaded from an external text file (words.txt).
    Difficulty Levels: Choose between easy, medium, and hard difficulty levels, affecting the number of allowed incorrect guesses.
    Add New Words: Players can add new words to the word list during gameplay.
    Unit Testing: Includes a test suite to verify the functionality of the game components.

Project Structure

bash

hangman/
│
├── hangman.py            # Main game code
├── words.txt             # Text file containing everyday words
└── test_hangman.py       # Test file for unit testing

How to Play

    Start the game by running hangman.py.
    Choose a difficulty level (easy, medium, or hard).
    Guess letters to try to uncover the hidden word.
    If you guess a letter correctly, it will be revealed in the word.
    If you guess incorrectly, you lose a try.
    The game ends when you either guess the word or run out of tries.
    After the game, you can add new words to the list.

Contributing

Elizabeth Sharon Zimba - Back-end and game logic. Feel free to submit issues or pull requests. Contributions are welcome!
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements

    -The classic game of Hangman, which inspired this project.
    -ALX for providing the learning platform for this project.