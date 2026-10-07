import random

def number_guessing_game():
    print("===== NUMBER GUESSING GAME =====")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")

        elif guess > secret_number:
            print("Too high! Try again.")

        else:
            print("Congratulations!")
            print("You guessed the number!")
            print("Number:", secret_number)
            print("Attempts:", attempts)
            break
def word_counter():
    print("\n===================================")
    print("       WORD FREQUENCY COUNTER")
    print("===================================")

    filename = input("Enter the text file name: ")

    try:
        with open(filename, "r") as file:
            text = file.read()

    except FileNotFoundError:
        print("File not found!")
        return

    text = text.lower()

  
    import string
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    
    words = text.split()

    print("\nTotal words:", len(words))

   
    word_frequency = {}

    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1

    print("\nWord Frequency:")

    for word, count in word_frequency.items():
        print(word, ":", count)
while True:
    print("\n1. Number Guessing Game")
    print("2. Word Frequency Counter")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        number_guessing_game()

    elif choice == "2":
        word_counter()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")