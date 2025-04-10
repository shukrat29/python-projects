import random

def roll_dice(amount: int = 2) -> list[int]:
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    rolls: list[int] = []
    for i in range(amount):
        random_roll: int = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls  # Return should not be inside the loop


def main():
    while True:
        try:
            user_input: str = input("How many dice would you like to roll? (Type 'exit' to quit): ")

            if user_input.lower() == "exit":
                print("Thanks for playing😊")
                break

            print(*roll_dice(int(user_input)), sep=" , ")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
