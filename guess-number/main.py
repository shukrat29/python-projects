from random import randint

lower_num, higher_num = 1, 10
random_number: int = randint(lower_num, higher_num)

print(f"Guess a number between {lower_num} and {higher_num}")

while True:
    try:
        user_guess: int = int(input("Enter your guess: "))
        
        if user_guess > random_number:
            print("Guess lower")
        elif user_guess < random_number:
            print("Guess higher")
        else:
            print("You guessed it right!")
            break

    except ValueError:
        print("Invalid input. Please enter a valid number.")
