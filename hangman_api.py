
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Mock database for games
games = {}

# Mock word list
words = ["apple", "banana", "grape", "orange", "peach"]

# API Documentation Route
@app.route('/api/v1/docs', methods=['GET'])
def get_api_docs():
    """Provide documentation for the Hangman API."""
    documentation = {
        "title": "Hangman API Documentation",
        "description": "This API allows users to play a simple game of Hangman.",
        "base_url": "http://localhost:5000/api/v1",
        "endpoints": [
            {
                "method": "POST",
                "url": "/game/start",
                "description": "Starts a new game of Hangman.",
                "request_body": {
                    "difficulty": "easy | medium | hard"
                },
                "response": {
                    "game_id": "integer",
                    "word": "string (the word to guess)",
                    "remaining_tries": "integer",
                    "current_status": "string (current state of the word)"
                },
                "success_code": 201,
                "error_code": 400
            },
            {
                "method": "POST",
                "url": "/game/<game_id>/guess",
                "description": "Submits a letter guess for the current game.",
                "request_body": {
                    "letter": "string (a single letter)"
                },
                "response": {
                    "current_status": "string",
                    "remaining_tries": "integer",
                    "message": "string (result of the guess)"
                },
                "success_code": 200,
                "error_code": 400
            },
            {
                "method": "GET",
                "url": "/game/<game_id>",
                "description": "Retrieves the current status of the game.",
                "response": {
                    "game_id": "integer",
                    "current_status": "string",
                    "remaining_tries": "integer",
                    "word": "string (the word to guess)"
                },
                "success_code": 200,
                "error_code": 404
            },
            {
                "method": "DELETE",
                "url": "/game/<game_id>",
                "description": "Ends the game and reveals the word.",
                "success_code": 204,
                "error_code": 404
            }
        ]
    }
    return jsonify(documentation), 200


# Route to start a new game
@app.route('/game/start', methods=['POST'])
def start_game():
    """Start a new game of Hangman."""
    data = request.get_json()
    difficulty = data.get('difficulty', 'easy')

    # Choose a word based on difficulty (for now, just random)
    word = random.choice(words)

    # Create a game_id and store the game state
    game_id = len(games) + 1
    games[game_id] = {
        'word': word,
        'remaining_tries': 6,  # Can vary based on difficulty
        'current_status': '_' * len(word),
        'guessed_letters': []
    }

    return jsonify({
        'game_id': game_id,
        'word': games[game_id]['current_status'],  # Masked word
        'remaining_tries': games[game_id]['remaining_tries'],
        'current_status': games[game_id]['current_status']
    }), 201


# Route to submit a letter guess
@app.route('/game/<int:game_id>/guess', methods=['POST'])
def make_guess(game_id):
    """Submit a letter guess for the current game."""
    data = request.get_json()
    letter = data.get('letter').lower()

    # Validate game existence
    if game_id not in games:
        return jsonify({"error": "Game not found"}), 404

    game = games[game_id]

    # Check if the game is already over
    if game['remaining_tries'] <= 0:
        return jsonify({
            "message": "Game over! No remaining tries.",
            "current_status": game['current_status'],
            "remaining_tries": game['remaining_tries']
        }), 400

    # Check if the letter was already guessed
    if letter in game['guessed_letters']:
        return jsonify({
            "message": f"'{letter}' was already guessed.",
            "current_status": game['current_status'],
            "remaining_tries": game['remaining_tries']
        }), 400

    game['guessed_letters'].append(letter)

    if letter in game['word']:
        # Reveal guessed letter in the word
        new_status = ''.join([letter if game['word'][i] == letter else game['current_status'][i] for i in range(len(game['word']))])
        game['current_status'] = new_status

        # Check if the game is won
        if '_' not in new_status:
            return jsonify({
                "message": "Congratulations! You've won!",
                "current_status": new_status,
                "remaining_tries": game['remaining_tries']
            }), 200
    else:
        # Wrong guess, decrease remaining tries
        game['remaining_tries'] -= 1

    return jsonify({
        "current_status": game['current_status'],
        "remaining_tries": game['remaining_tries'],
        "message": "Correct guess!" if letter in game['word'] else "Incorrect guess!"
    }), 200


# Route to retrieve game status
@app.route('/game/<int:game_id>', methods=['GET'])
def get_game_status(game_id):
    """Retrieve the current status of the game."""
    if game_id not in games:
        return jsonify({"error": "Game not found"}), 404

    game = games[game_id]
    return jsonify({
        "game_id": game_id,
        "current_status": game['current_status'],
        "remaining_tries": game['remaining_tries'],
        "word": game['word']
    }), 200


# Route to end the game
@app.route('/game/<int:game_id>', methods=['DELETE'])
def end_game(game_id):
    """End the game and reveal the word."""
    if game_id not in games:
        return jsonify({"error": "Game not found"}), 404

    word = games[game_id]['word']
    del games[game_id]

    return jsonify({
        "message": "Game ended.",
        "word": word
    }), 204


if __name__ == '__main__':
    app.run(debug=True)