from art import logo

print(logo)

print("Welcome To The Number guessing Game!")
print("I\'m thinking of a number between 1 and 100.")

attempts = 0
def select_difficulty():
    difficulty = input("Choose a difficulty level. Type 'e' for easy or 'h' for hard: ")
    global attempts
    if difficulty == 'e':
        attempts = 10
    elif difficulty == 'h':
        attempts = 5
    else:
        print("You have chosen an invalid command.")
        select_difficulty()

select_difficulty()

#print(f"You have {attempts} remaining to guess the correct number")

