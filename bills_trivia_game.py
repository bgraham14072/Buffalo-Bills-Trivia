import json
import random
import time
from collections import defaultdict

class BillsTrivia:
    def __init__(self):
        with open('bills_trivia_questions.json', 'r') as f:
            self.questions = json.load(f)
        self.leaderboard = defaultdict(int)
        self.current_player = None
        self.registered_users = set()  # Store registered usernames

    def start_game(self):
        print("Welcome to Buffalo Bills Trivia!")
        while True:
            choice = input("1. Register\n2. Login\nEnter your choice (1 or 2): ")
            if choice == '1':
                self.register_user()
            elif choice == '2':
                if self.login_user():
                    break
            else:
                print("Invalid choice. Please enter 1 or 2.")

        difficulties = ['easy', 'medium', 'hard']
        for difficulty in difficulties:
            print(f"\nStarting {difficulty.capitalize()} Round!")
            self.play_round(difficulty)

        print("\nGame Over!")
        self.display_score()
        self.update_leaderboard()

    def register_user(self):
        while True:
            username = input("Enter a new username: ")
            if username in self.registered_users:
                print("Username already exists. Please choose another.")
            else:
                self.registered_users.add(username)
                print(f"User {username} registered successfully!")
                break

    def login_user(self):
        username = input("Enter your username: ")
        if username in self.registered_users:
            self.current_player = username
            print(f"Welcome back, {username}!")
            return True
        else:
            print("Username not found. Please register first.")
            return False

    # ... (rest of the class methods remain the same)

if __name__ == "__main__":
    game = BillsTrivia()
    game.start_game()
