import random

def tas_kagit_makas(name):
    user_score = 0
    computer_score = 0
    rounds = 3

    print("The game will be 3 rounds, and if you win 2, you win the game! Also, if you don't want to play, type 'exit' at any time.")
    print("To choose Rock, type 'R'\nTo choose Paper, type 'P'\nTo choose Scissors, type 'S'\n")

    for _ in range(rounds):
        computer_attack = random.randint(1, 3)  # 1=Rock, 2=Paper, 3=Scissors
        attack = input("Your move: ").upper()  # for 'r', 'R', etc.

        if attack == 'EXIT':
            print("Exiting the game. Thanks for playing!")
            break

        if attack not in ['R', 'P', 'S']:
            print("Invalid input. Please enter 'R', 'P', or 'S'.")
            continue

        # Check for the result of the round
        if (attack == 'R' and computer_attack == 1) or (attack == 'P' and computer_attack == 2) or (attack == 'S' and computer_attack == 3):
            print("Tie! No points awarded.")
        elif (attack == 'R' and computer_attack == 3) or (attack == 'P' and computer_attack == 1) or (attack == 'S' and computer_attack == 2):
            user_score += 1
            print(f"You won this round! You're so lucky.\nScore: {user_score}-{computer_score}")
        else:
            computer_score += 1
            print(f"I won this round!\nScore: {user_score}-{computer_score}")

        if user_score == 2 or computer_score == 2:
            break

    if user_score > computer_score:
        print(f"Congratulations, {name}! You won the game with a score of {user_score}-{computer_score}.")
    else:
        print(f"Sorry, {name}. I won the game with a score of {computer_score}-{user_score}.")

def main():
    print("Welcome to Rock-Paper-Scissors!\nPlease enter your nickname:")
    name = input()

    while True:
        print("Please select an option:\n1. Start the game\n0. Exit")
        section = input()

        if section == '1':
            print("The game is starting...")
            tas_kagit_makas(name)
        elif section == '0':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid input. Please enter '1' to start the game or '0' to exit.")

        # Asking if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye!")
            break

# Directly calling main() at the end
main()