import string
def main(word):
    word = word.upper().strip()
    guessed_letters = []
    count = 0
    check = []
    incorrect_guesses_count = 0
    hidden_word = welcome(word)
    while incorrect_guesses_count <= 5:
        guessed_letter = guess_input(check)
        check.append(guessed_letter)
        index_letter = []
        if guessed_letter in word:
            index_letter = [index for index in range(len(word)) if guessed_letter == word[index]]
            for index in index_letter:
                hidden_word = hidden_word[:index] + word[index] + hidden_word[index + 1:]
        else:
            print("Incorrect!")
            incorrect_guesses_count += 1
        print(hidden_word + "\t" + str(6 - incorrect_guesses_count) + " Guesses Left")
        if hidden_word == word:
            print("Congratulations! You Won!")
            return
    print(f"The word was: {word}")
    return

def welcome(word):
    print("Welcome to Hangman !")
    hidden_word = "_" * len(word)
    print(hidden_word)
    return hidden_word

def guess_input(check):
    while True:
        guess = input("Guess your letter: ").strip().upper()
        if guess in check:
            print("You already played that letter! Try again!")
            continue
        elif guess in range(10):
            guess = int(guess)
            print("Don't use a number! use a letter! try again!")
            continue
        elif guess not in list(string.ascii_uppercase):
            print("Use a letter in the alphabet!")
            continue
        elif len(guess) > 1:
            print("Use only a single letter! retry!")
            continue
        else:
            return guess

if __name__ == "__main__":
    main("Ventilation")