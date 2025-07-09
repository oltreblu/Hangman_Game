import Guess_Letters as game
import Pick_Word as random_word
def main():
    while True:
        hidden_word = random_word.main()
        game.main(hidden_word)
        if not input("Do you want to start another game?(Press Enter to exit, enter anything else to continue) "):
            break

main()