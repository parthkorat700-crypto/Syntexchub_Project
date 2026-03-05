import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0

    print("\nGuess the number between 1 and 100")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > number:
            print("Too High!")

        elif guess < number:
            print("Too Low!")

        else:
            print("Correct! You guessed in", attempts, "attempts.")
            break


while True:
    play_game()

    again = input("Play again? (yes/no): ")

    if again.lower() != "yes":
        print("Thanks for playing!")
        break