Hangman Game
Console Game
Overview

The console-based Hangman game allows users to play the classic game directly from the terminal. This component of the project demonstrates basic programming concepts including loops, conditionals, and file handling.
Features

    Core Gameplay: Guess letters to reveal a hidden word.
    Dynamic Word Selection: Words are loaded from an external text file (words.txt).
    Difficulty Levels: Choose between easy, medium, and hard difficulty levels.
    Add New Words: Add new words to the list during gameplay.
    Unit Testing: Includes tests to verify functionality.

Installation and Usage

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

Run the Console Game:

bash

python hangman.py

Running Tests:

bash

    python -m unittest test_hangman.py

How to Play

    Start the game by running hangman.py.
    Choose a difficulty level (easy, medium, or hard).
    Guess letters to try to uncover the hidden word.
    The game ends when you either guess the word or run out of tries.
    After the game, you can add new words to the list.

Hangman API
Introduction

The Hangman API provides RESTful endpoints to interact with a Hangman game programmatically. Users can start new games, submit guesses, retrieve the current game status, and end the game.
Base URL

For the API:

bash

http://localhost:5000/api/v1

Endpoints
1. Start a New Game

    Method: POST
    URL: /game/start
    Description: Starts a new game of Hangman.
    Request Body:

    json

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
        Success (204 No Content): No content returned.
        Error (404 Not Found):

        json

        {
          "error": "Game not found"
        }

Error Handling

    400 Bad Request: Invalid request parameters.
    404 Not Found: Requested resource does not exist.
    500 Internal Server Error: Unexpected server error.

Rate Limiting

    Each user can make up to 100 requests per hour.

Contributing

    Elizabeth Sharon Zimba: Back-end and game logic. Contributions are welcome! Feel free to submit issues or pull requests.

License

This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements

    The classic game of Hangman, which inspired this project.
    ALX for providing the learning platform for this project.