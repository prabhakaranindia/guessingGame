import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Guess a number between 1 and 100 (or type 'quit' to exit): ")
        if guess.lower() == 'quit':
            print("Thanks for playing! The number was", number_to_guess)
            break

        try:
            guess = int(guess)
            attempts += 1
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

number_guessing_game()
