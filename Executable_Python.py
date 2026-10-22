import random

def number_guessing_game():
    print("=== Number Guessing Game ===")

    # Let the player choose the range
    while True:
        try:
            minimum = int(input("Enter the minimum number: "))
            maximum = int(input("Enter the maximum number: "))

            if minimum >= maximum:
                print("Error: The maximum must be greater than the minimum.")
            else:
                break

        except ValueError:
            print("Invalid input. Please enter whole numbers.")

    # Generate a random secret number within the chosen range
    secret_number = random.randint(minimum, maximum)
    attempts = 0

    print(f"\nI have chosen a number between {minimum} and {maximum}.")
    print("Try to guess it!")

    # Let the player guess until the number is found
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < minimum or guess > maximum:
                print(f"Please choose a number between {minimum} and {maximum}.")
            elif guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nCongratulations! You guessed {secret_number}!")
                print(f"It took you {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    number_guessing_game()