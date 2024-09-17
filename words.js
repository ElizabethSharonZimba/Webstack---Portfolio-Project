const words = [
    'beautiful', 'hard', 'soft', 'computer', 'money', 'food'
];

function getRandomWord() {
    return words[Math.floor(Math.random() * words.length)];
}

module.exports = { getRandomWord };
