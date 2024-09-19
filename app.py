from flask import Flask, jsonify, request, abort
import random

app = Flask(__name__)

# In-memory store for game state
games = {}

# Route to start a new game
@app.route('/api/v1/game/start', methods=['POST'])
def start_game():
    """
    Starts a new game with a specified difficulty level.

    Request Body:
    - difficulty (str): The difficulty level for the game. Options are "easy", "medium", or "hard".

    Response:
    - game_id (str): A unique identifier for the game.
    - word_template (str): A string of underscores representing the hidden word.
    - attempts_left (int): Number of attempts left based on difficulty.
    """
    data = request.get_json()
    
    # Ensure difficulty level is provided
    if 'difficulty' not in data:
        abort(400, description="Difficulty level is required")
    
    difficulty = data['difficulty']
    
    # Set max attempts based on difficulty
    max_attempts = {'easy': 10, 'medium': 7, 'hard': 5}.get(difficulty, 5)
    
    # Sample word list for demonstration
    words = ["python", "flask", "hangman", "developer"]
    word = random.choice(words)  # Randomly select a word
    word_template = '_' * len(word)  # Initialize the word template with underscores
    
    # Generate a unique game ID and initialize game state
    game_id = str(random.randint(1000, 9999))
    games[game_id] = {
        'word': word,
        'word_template': word_template,
        'attempts_left': max_attempts,
        'guesses': set()
    }
    
    return jsonify({
        'game_id': game_id,
        'word_template': word_template,
        'attempts_left': max_attempts
    })

# Route to make a guess
@app.route('/api/v1/game/<game_id>/guess', methods=['POST'])
def make_guess(game_id):
    """
    Processes a letter guess in an ongoing game.

    Parameters:
    - game_id (str): The unique identifier of the game.

    Request Body:
    - letter (str): The letter being guessed.

    Response:
    - word_template (str): Updated word template with guessed letters revealed.
    - attempts_left (int): Remaining attempts.
    - message (str): Result message (e.g., "You won!" or "You lost!").
    """
    if game_id not in games:
        abort(404, description="Game not found")
    
    data = request.get_json()
    
    # Ensure letter is provided
    if 'letter' not in data:
        abort(400, description="Letter is required")
    
    letter = data['letter']
    game = games[game_id]
    
    # Check if the letter has already been guessed
    if letter in game['guesses']:
        return jsonify({'message': 'Letter already guessed'})
    
    # Update game state based on guess
    game['guesses'].add(letter)
    
    if letter in game['word']:
        game['word_template'] = ''.join(
            letter if letter == game['word'][i] else game['word_template'][i]
            for i in range(len(game['word']))
        )
    else:
        game['attempts_left'] -= 1
    
    # Check for win/loss conditions
    if '_' not in game['word_template']:
        return jsonify({'word_template': game['word_template'], 'attempts_left': game['attempts_left'], 'message': 'You won!'})
    
    if game['attempts_left'] <= 0:
        return jsonify({'word_template': game['word_template'], 'attempts_left': game['attempts_left'], 'message': 'You lost!'})

    return jsonify({'word_template': game['word_template'], 'attempts_left': game['attempts_left']})

# Route to check game status
@app.route('/api/v1/game/<game_id>', methods=['GET'])
def check_status(game_id):
    """
    Retrieves the current status of an ongoing game.

    Parameters:
    - game_id (str): The unique identifier of the game.

    Response:
    - word_template (str): The current word template with revealed letters.
    - attempts_left (int): Number of attempts left.
    - status (str): Game status (e.g., "in-progress").
    """
    if game_id not in games:
        abort(404, description="Game not found")
    
    game = games[game_id]
    return jsonify({
        'word_template': game['word_template'],
        'attempts_left': game['attempts_left'],
        'status': 'in-progress'
    })

# Route to end the game
@app.route('/api/v1/game/<game_id>', methods=['DELETE'])
def end_game(game_id):
    """
    Ends the specified game and removes it from the in-memory store.

    Parameters:
    - game_id (str): The unique identifier of the game.

    Response:
    - message (str): Confirmation message that the game has been ended.
    """
    if game_id not in games:
        abort(404, description="Game not found")
    
    del games[game_id]
    return jsonify({'message': 'Game ended successfully'})

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
