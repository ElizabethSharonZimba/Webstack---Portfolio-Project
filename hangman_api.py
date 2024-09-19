
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
    """Provide documentation for the Hangman API.

    This endpoint returns a JSON object describing the available API endpoints,
    their methods, request and response formats, and possible success and error codes.

    Returns:
        response (JSON): API documentation.
        status_code (int): HTTP status code (200 OK).
    """
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
    """Start a new game of Hangman.

    This endpoint initializes a new game with a randomly selected word and
    stores the game state in a mock database. It returns the initial game state,
    including the masked word and the number of remaining tries.

    Returns:
        response (JSON): Initial game state including game_id, masked word,
                          remaining tries, and current status.
        status_code (int): HTTP status code (201 Created).
    """
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
    """Submit a letter guess for the current game.

    This endpoint processes a letter guess, updates the game state, and returns
    the current game status, including the updated word status and remaining tries.
    It handles both correct and incorrect guesses and checks if the game is won.

    Args:
        game_id (int): ID of the game.

    Returns:
        response (JSON): Current game status including current status, remaining
                          tries, and a message indicating the result of the guess.
        status_code (int): HTTP status code (200 OK) for valid input, (400 Bad Request)
                           for invalid guesses, or (404 Not Found) if the game is not found.
    """
    data = request.get_json()
    letter = data.get('letter').lower()

    # Validate game existence
    if game_id not in games:
        return jsonify({"error": "Game not found"}), 404

    game = games[game_id]
    
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
    """Retrieve the current status of the game.

    This endpoint returns the current state of the game, including the masked word,
    remaining tries, and the original word.

    Args:
        game_id (int): ID of the game.

    Returns:
        response (JSON): Current game status including game_id, current status,
                          remaining tries, and the word to guess.
        status_code (int): HTTP status code (200 OK) if the game exists, or (404 Not Found)
                           if the game is not found.
    """
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
    """End the game and reveal the word.

    This endpoint ends the game, deletes its state from the mock database, and returns
    the word that was being guessed.

    Args:
        game_id (int): ID of the game.

    Returns:
        response (JSON): Message indicating the game has ended and the word that was being guessed.
        status_code (int): HTTP status code (204 No Content) if the game is successfully ended,
                           or (404 Not Found) if the game is not found.
    """
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
    app.run(debug=True, port=5000)