const express = require('express');
const app = express();
const path = require('path');
const words = require('./words');

// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Serve index.html for the root route
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

let currentWord;
let guessedLetters;
let remainingGuesses;

function initializeGame() {
    currentWord = words.getRandomWord();
    guessedLetters = [];
    remainingGuesses = 6;
}

app.get('/new-game', (req, res) => {
    initializeGame();
    res.json({
        word: '_'.repeat(currentWord.length),
        remainingGuesses,
        guessedLetters,
    });
});

app.get('/guess/:letter', (req, res) => {
    const letter = req.params.letter.toLowerCase();
    if (!guessedLetters.includes(letter) && remainingGuesses > 0) {
        guessedLetters.push(letter);
        if (!currentWord.includes(letter)) {
            remainingGuesses--;
        }
    }

    const maskedWord = currentWord
        .split('')
        .map((char) => (guessedLetters.includes(char) ? char : '_'))
        .join('');

    res.json({
        word: maskedWord,
        remainingGuesses,
        guessedLetters,
        gameOver: maskedWord === currentWord || remainingGuesses === 0,
        win: maskedWord === currentWord,
    });
});

// Start the server
const port = 3000;
app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
