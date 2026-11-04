import random

def number_guessing_game():
    print("=== Szám kitaláló játék ===")

    while True:
        try:
            minimum = int(input("Írjon be egy Minimum értéket: "))
            maximum = int(input("Írjon be egy Maximum értéket: "))

            if minimum >= maximum:
                print("Hiba: A Maximum szám nem lehet alacsonyabb mint a Minimum szám.")
            else:
                break

        except ValueError:
            print("Helytelen Bemenet. Adjon meg egy egész számot.")

    # Generate a random secret number within the chosen range
    secret_number = random.randint(minimum, maximum)
    attempts = 0

    print(f"\nEgy szám kiválasztásra került {minimum} és {maximum} között.")
    print("Pobáld meg kitalálni!")

    # Let the player guess until the number is found
    while True:
        try:
            guess = int(input("A tipped: "))
            attempts += 1

            if guess < minimum or guess > maximum:
                print(f"Adjon meg egy számot {minimum} és {maximum} között.")
            elif guess < secret_number:
                print("Túl alacsony! Probáljon magasabb számot.")
            elif guess > secret_number:
                print("Túl magas! Próbáljon alacsonyabb számot.")
            else:
                print(f"\nNyertél! Kitaláltad a(z) {secret_number} számot!")
                print(f"{attempts} próbálkozásba telt.")
                break

        except ValueError:
            print("Helytelen Bemenet. Adjon meg egy egész számot")


if __name__ == "__main__":
    number_guessing_game()