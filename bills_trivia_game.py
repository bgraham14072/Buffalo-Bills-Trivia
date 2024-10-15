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

    def start_game(self):
        print("Welcome to Buffalo Bills Trivia!")
        self.current_player = input("Enter your username: ")
        
        difficulties = ['easy', 'medium', 'hard']
        for difficulty in difficulties:
            print(f"\nStarting {difficulty.capitalize()} Round!")
            self.play_round(difficulty)

        print("\nGame Over!")
        self.display_score()
        self.update_leaderboard()

    def play_round(self, difficulty):
        questions = random.sample(self.questions[difficulty], 5)  # Play 5 questions per round
        for q in questions:
            print(f"\n{q['question']}")
            for i, option in enumerate(q['options'], 1):
                print(f"{i}. {option}")

            start_time = time.time()
            answer = input("Your answer (1-4): ")
            end_time = time.time()

            if answer.isdigit() and 1 <= int(answer) <= 4:
                if q['options'][int(answer)-1] == q['correct_answer']:
                    points = self.calculate_points(difficulty, end_time - start_time)
                    print(f"Correct! You earned {points} points.")
                    self.leaderboard[self.current_player] += points
                else:
                    points = self.calculate_negative_points(difficulty)
                    print(f"Incorrect. You lost {abs(points)} points.")
                    self.leaderboard[self.current_player] += points
            else:
                print("Invalid input. No points awarded.")

    def calculate_points(self, difficulty, time_taken):
        base_points = {'easy': 100, 'medium': 200, 'hard': 500}
        points = base_points[difficulty]
        if time_taken <= 10:
            points += 50  # Bonus for answering within 10 seconds
        return points

    def calculate_negative_points(self, difficulty):
        return {'easy': -50, 'medium': -100, 'hard': -250}[difficulty]

    def display_score(self):
        print(f"\n{self.current_player}'s Final Score: {self.leaderboard[self.current_player]}")

    def update_leaderboard(self):
        print("\nLeaderboard:")
        sorted_leaderboard = sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)
        for i, (player, score) in enumerate(sorted_leaderboard[:5], 1):
            print(f"{i}. {player}: {score}")

if __name__ == "__main__":
    game = BillsTrivia()
    game.start_game()
