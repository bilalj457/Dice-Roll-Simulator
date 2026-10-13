import random

roll_count = 0

print("Welcome to the Dice Rolling Simulator!")

while True:
    choice = input("Do you want to roll the dice? (yes/no): ").lower()

    if choice == "yes":
        dice = random.randint(1, 6)
        roll_count += 1

        print("You rolled:", dice)
        print("Total rolls:", roll_count)

    elif choice == "no":
        print("Thanks for playing!")
        print("You rolled the dice", roll_count, "times.")
        break

    else:
        print("Please enter yes or no.")
