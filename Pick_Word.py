import random
def main():
    with open('sowpods.txt','r') as file:
        file_text = file.read().split("\n")
    return random.choice(file_text)

if __name__ == "__main__":
    random_word = main()
    print(random_word)