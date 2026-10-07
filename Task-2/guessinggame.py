import random

def guessing_game():
    print("\n===== NUMBER GUESSING GAME =====")

    number = random.randint(1, 100)
    attempts = 0
    score = 100

    print("I have chosen a number between 1 and 100.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue

        if guess < number:
            print("Too low! Try again.")

        elif guess > number:
            print("Too high! Try again.")

        else:
            print("\nCongratulations!")
            print("You guessed the number:", number)
            print("Attempts:", attempts)

            
            score = max(10, 100 - (attempts - 1) * 10)

            print("Your score:", score)
            break


guessing_game()