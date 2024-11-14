
import random

class HighLowGame:
    def __init__(self):
        self.score = 0  

    def play_round(self):
        player_number = random.randint(0, 99)
        computer_number = random.randint(0, 99)
        print(f"\nYour number is {player_number}")
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()

        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print(f"You were right! The computer's number was {computer_number}")
            self.score += 1
        else:
            print(f"Incorrect! The computer's number was {computer_number}")

class GuessNumberGame:
    def __init__(self):
        self.score = 0  
        self.secret_number = None

    def reset_game(self):
        self.secret_num()

    def secret_num(self):
        self.secret_number = random.randint(0, 99)

    def play_round(self):
        rounds = int(input("How many attempts would you like to have? "))
        attempts = 0
        
        while attempts < rounds:
            try:
                guess = int(input("Guess a number between 0 and 99: "))
                attempts += 1
                if guess < self.secret_number:
                    print("Your guess is too low.")
                elif guess > self.secret_number:
                    print("Your guess is too high.")
                else:
                    print(f"Congrats! You guessed the number {self.secret_number} in {attempts} attempts.")
                    break
            except ValueError:
                print("Please enter a valid number.")

class Game:
    def __init__(self):
        self.player_name = ""  
        self.high_low_game = HighLowGame()  
        self.guess_number_game = GuessNumberGame()  

    def play_game(self):
        self.player_name = input("Enter your name: ")
        print(f"\nWelcome, {self.player_name}!")  

        while True:
            choice = input("\nChoose a game to play:\n1. High-Low Game\n2. Guess My Number\n3. Exit\nEnter your choice: ")

            if choice == "1":
                while True:
                    try:
                        rounds = int(input("How many rounds would you like to play in the High-Low Game? "))
                        break
                    except ValueError:
                        print("Please enter a valid number.")
                
                print("\nStarting the High-Low Game!")
                for _ in range(rounds):  
                    self.high_low_game.play_round()
                print(f"\n{self.player_name}, your final score for the High-Low Game is: {self.high_low_game.score}")

            elif choice == "2":
                print("\nStarting the Guess My Number Game!")
                self.guess_number_game.reset_game()  
                self.guess_number_game.play_round()  

            elif choice == "3":
                print(f"Thanks for playing, {self.player_name}! See you next time.")
                break

            else:
                print("Invalid choice. Please select again.")

game_controller = Game()
game_controller.play_game()