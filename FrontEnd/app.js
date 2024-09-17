let wordDisplay = document.getElementById('word');
let remainingDisplay = document.getElementById('remaining');
let guessedDisplay = document.getElementById('guessed');
let statusDisplay = document.getElementById('status');
let letterInput = document.getElementById('letterInput');
let guessBtn = document.getElementById('guessBtn');
let resetBtn = document.getElementById('resetBtn');

let gameState = {
    word: '',
    remainingGuesses: 6,
    guessedLetters: []
};

function fetchNewGame() {
    fetch('/new-game')
        .then(response => response.json())
        .then(data => updateGameState(data));
}

function updateGameState(data) {
    gameState.word = data.word;
    gameState.remainingGuesses = data.remainingGuesses;
    gameState.guessedLetters = data.guessedLetters;
    
    wordDisplay.textContent = gameState.word;
    remainingDisplay.textContent = `Remaining Guesses: ${gameState.remainingGuesses}`;
    guessedDisplay.textContent = `Guessed Letters: ${gameState.guessedLetters.join(', ')}`;
    statusDisplay.textContent = '';
}

function makeGuess(letter) {
    fetch(`/guess/${letter}`)
        .then(response => response.json())
        .then(data => {
            updateGameState(data);
            if (data.gameOver) {
                if (data.win) {
                    statusDisplay.textContent = 'Congratulations! You won!';
                } else {
                    statusDisplay.textContent = 'Game over! You lost!';
                }
            }
        });
}

guessBtn.addEventListener('click', () => {
    const letter = letterInput.value.toLowerCase();
    if (letter && !gameState.guessedLetters.includes(letter)) {
        makeGuess(letter);
    }
    letterInput.value = '';
});

resetBtn.addEventListener('click', fetchNewGame);

fetchNewGame();
