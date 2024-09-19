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
we will be using the cURL commands

cURL

Start a New Game:

bash(on a terminal use the following cURL comands to pay the game)

curl -X POST http://localhost:5000/game/start -H "Content-Type: application/json" -d '{"difficulty": "easy"}'

Make a Guess:

bash

curl -X POST http://localhost:5000/game/<game_id>/guess -H "Content-Type: application/json" -d '{"letter": "a"}'

Replace <game_id> with the actual game ID from the response of the start game request.

Check Game Status:

bash

curl -X GET http://localhost:5000/game/<game_id>

Replace <game_id> with the actual game ID.

End the Game:

bash

curl -X DELETE http://localhost:5000/game/<game_id>

Replace <game_id> with the actual game ID.
HTTPie

Start a New Game:

bash

http POST http://localhost:5000/game/start difficulty=easy

Make a Guess:

bash

http POST http://localhost:5000/game/<game_id>/guess letter=a

Replace <game_id> with the actual game ID.

Check Game Status:

bash

http GET http://localhost:5000/game/<game_id>

Replace <game_id> with the actual game ID.

End the Game:

bash

http DELETE http://localhost:5000/game/<game_id>

Replace <game_id> with the actual game ID.

1. Start a New Game

To begin a new game, send a POST request to the /game/start endpoint. You need to specify the difficulty level in the request body.
Request:

    Method: POST
    URL: http://127.0.0.1:5000/api/v1/game/start
    Body (JSON):

    json

    {
      "difficulty": "easy"
    }

    You can choose between "easy", "medium", and "hard".

Response:

    game_id: Unique identifier for the game session.
    word_template: The hidden word with underscores for each unrevealed letter.
    attempts_left: Number of wrong guesses remaining.

2. Make a Guess

To guess a letter, send a POST request to the /game/<game_id>/guess endpoint. Replace <game_id> with the ID you received when starting the game.
Request:

    Method: POST
    URL: http://127.0.0.1:5000/api/v1/game/<game_id>/guess
    Body (JSON):

    json

    {
      "letter": "a"
    }

Response:

    word_template: The updated word showing correctly guessed letters.
    attempts_left: Remaining wrong guesses.
    message: Feedback on the guess (e.g., "Good guess!" or "Incorrect guess").

3. Check Game Status

At any time, you can check the current status of the game by sending a GET request to the /game/<game_id> endpoint.
Request:

    Method: GET
    URL: http://127.0.0.1:5000/api/v1/game/<game_id>

Response:

    word_template: Current state of the word.
    attempts_left: Remaining wrong guesses.
    status: Indicates if the game is still "in-progress" or has "won" or "lost."

4. End the Game

If you want to stop the game early, you can send a DELETE request to the /game/<game_id> endpoint.
Request:

    Method: DELETE
    URL: http://127.0.0.1:5000/api/v1/game/<game_id>

Response:

    message: Confirmation that the game has ended successfully.

bash
http://127.0.0.1:5000/api/v1/docs



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