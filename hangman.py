import random
from colorama import Fore, Style

def load_words():
    """Load words from a text file."""
    with open('words.txt', 'r') as file:
        return [line.strip().upper() for line in file.readlines()]

def display_hangman(tries):
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
    """Choose difficulty level and return number of tries."""
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
    """Add a new word to the words file."""
    new_word = input("Enter a new word to add: ").strip().upper()
    with open('words.txt', 'a') as file:
        file.write(new_word + '\n')
    print(Fore.GREEN + f"{new_word} has been added to the word list." + Style.RESET_ALL)

def fill_in_char(original_word, answer_word, char):
    """Fill in a missing character in the answer word based on the original word."""
    origi = list(original_word)
    answ = list(answer_word)

    for i in range(len(origi)):
        if char == origi[i]:
            answ[i] = char

    return ''.join(answ)

def play():
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