Project Overview

The Hangman game is a classic word-guessing game where the player has to guess a hidden word by suggesting letters within a certain number of guesses. This project is a web-based implementation of the Hangman game, designed with a front-end for user interaction and a back-end API for game logic.
Features

    Guess letters to uncover a randomly chosen word.
    Track remaining guesses and letters already guessed.
    Win the game by guessing all letters or lose if guesses run out.
    Reset the game and start with a new word anytime.
    Responsive design for optimal user experience across devices.

Technologies Used
Front-end

    HTML: Structure of the web page.
    CSS: Styling and layout.
    JavaScript: Game logic and interaction with the back-end API.

Back-end

    Node.js: Server-side JavaScript runtime.
    Express.js: Framework for building the back-end API.

Development Tools

    Git: Version control.
    Visual Studio Code: Code editor.
    Postman: For testing API endpoints.

Setup and Installation
Prerequisites

    Node.js installed on your machine.
    A browser to run the front-end.

Steps

    Clone the repository:

    bash

git clone  https://github.com/ElizabethSharonZimba/Webstack---Portfolio-Project.git
cd hangman-game

Install dependencies: In the project directory, run the following command:

bash

npm install

Start the back-end server:

bash

    node server.js

    Run the front-end: Open index.html in your browser.

    The back-end will run on http://localhost:3000, and the front-end will connect to it automatically.

Usage

    Start the Game: Once the front-end is loaded, a word will be chosen at random, and you’ll see underscores representing the hidden word.
    Make a Guess: Enter a letter and press "Guess." The game will reveal any correct guesses in the word or reduce the remaining guesses if the letter is incorrect.
    Win or Lose: You win by guessing all letters before running out of guesses. You lose if all guesses are used up.
    Reset the Game: Click "Reset Game" to start a new round with a new word.

Game Logic

    Word Selection: A random word is chosen from a predefined list when the game starts.
    Guesses: Players have a total of 6 incorrect guesses before they lose the game.
    Letter Validation: The game checks if a guessed letter is in the word and updates the display accordingly.
    Game End: The game ends when:
        All letters are correctly guessed (win).
        The player runs out of guesses (loss).

Future Improvements

Some possible enhancements include:

    Word Difficulty Levels: Add easy, medium, and hard words based on length or complexity.
    Multiplayer Mode: Allow two players to take turns guessing letters.
    Themes: Add different themes to the game, like animals, countries, or movies.
    Score Tracking: Implement a database to save high scores or player stats.
Contributors

    Elizabeth Sharon Zimba - Back-end and game logic.
    			   - Front-end and design.

If you'd like to contribute, feel free to open a pull request or submit an issue.
License

This project is licensed under the MIT License. See the LICENSE file for more details.
Acknowledgements

    The classic game of Hangman, which inspired this project.
    ALX for providing the learning platform for this project.


