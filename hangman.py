import random
from colorama import Fore, Style

def load_words():
    """Load words from a text file.

    Reads a list of words from 'words.txt', converts them to uppercase,
    and returns them as a list of strings.

    Returns:
        list: A list of words in uppercase from the file.
    """
    with open('words.txt', 'r') as file:
        return [line.strip().upper() for line in file.readlines()]

def display_hangman(tries):
    """Return the current hangman stage based on the number of remaining tries.

    Args:
        tries (int): Number of tries left.

    Returns:
        str: The hangman drawing corresponding to the number of tries left.
    """
    stages = [
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        """,
        """
           ------
           |    |
           |
           |
           |
           |
        """,
        """
           ------
           |
           |
           |
           |
           |
        """,
    ]
    return stages[tries]

def choose_difficulty():
    """Prompt the user to choose a difficulty level and return the corresponding number of tries.

    Returns:
        int: Number of tries based on user choice (6 for Easy, 4 for Medium, 3 for Hard).
    """
    print(Fore.CYAN + "Choose difficulty level:" + Style.RESET_ALL)
    print(Fore.CYAN + "1. Easy (10 tries)" + Style.RESET_ALL)
    print(Fore.CYAN + "2. Medium (7 tries)" + Style.RESET_ALL)
    print(Fore.CYAN + "3. Hard (5 tries)" + Style.RESET_ALL)
    
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 6
        elif choice == '2':
            return 4
        elif choice == '3':
            return 3
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)

def add_word():
    """Prompt the user to enter a new word and add it to the 'words.txt' file.

    The word is converted to uppercase before being added.
    """
    new_word = input("Enter a new word to add: ").strip().upper()
    with open('words.txt', 'a') as file:
        file.write(new_word + '\n')
    print(Fore.GREEN + f"{new_word} has been added to the word list." + Style.RESET_ALL)

def fill_in_char(original_word, answer_word, char):
    """Fill in the missing characters in the answer word based on the guessed character.

    Args:
        original_word (str): The word to guess.
        answer_word (str): The current state of the guessed word.
        char (str): The character to fill in.

    Returns:
        str: Updated answer word with the guessed character filled in.
    """
    origi = list(original_word)
    answ = list(answer_word)

    for i in range(len(origi)):
        if char == origi[i]:
            answ[i] = char

    return ''.join(answ)

def play():
    """Main function to play the Hangman game.

    - Loads words from the file.
    - Selects a random word for the game.
    - Prompts the user to guess letters.
    - Displays the current state of the hangman and word.
    - Manages the number of tries and guessed letters.
    - Ends the game when the word is guessed or tries run out.
    """
    print(Fore.CYAN + "Let's play Hangman!" + Style.RESET_ALL)
    
    words = load_words()
    word = random.choice(words)
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = choose_difficulty()

    while not guessed and tries > 0:
        print(display_hangman(tries))
        print(Fore.YELLOW + word_completion + Style.RESET_ALL)  
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        guess = input("Please guess a letter: ").upper()

        if len(guess) == 1 and guess.isalpha(): 
            if guess in guessed_letters:
                print(Fore.RED + "You already guessed that letter." + Style.RESET_ALL)
            elif guess not in word:
                print(Fore.RED + f"{guess} is not in the word." + Style.RESET_ALL)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(Fore.GREEN + f"Good job! {guess} is in the word." + Style.RESET_ALL)
                guessed_letters.append(guess)
                word_completion = fill_in_char(word, word_completion, guess)
                if "_" not in word_completion:
                    guessed = True
        else:
            print(Fore.RED + "Invalid input. Please try again." + Style.RESET_ALL)

    if guessed:
        print(Fore.YELLOW + f"Congratulations! You guessed the word: {word}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Sorry, you ran out of tries. The word was: {word}" + Style.RESET_ALL)

if __name__ == "__main__":
    while True:
        play()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            break
        add_word_choice = input("Do you want to add a new word? (yes/no): ").lower()
        if add_word_choice == 'yes':
            add_word()
