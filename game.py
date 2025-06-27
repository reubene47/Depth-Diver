import time
import random
import csv
import os
from functions import (
    clear_screen, format_time, save_score, show_leaderboard,
    run_event
)

# Main Game
clear_screen()
print("🌊 Welcome to Depth Diver! The Deep Logic Dive 🌊")
player = input("What's your name, diver? ").strip().title()

total_oxygen = 120 # start with 2 minutes of oxygen
start_time = time.time()
depth = 1 # start at depth 1
oxygen_penalty = 10  # seconds penalty for wrong answers
final_question_mode = False # when time runs out there is a final question
last_result = ""
shipwreck_message = ""

print(f"\nHi {player}, your dive lasts 2 minutes. Good luck!\n")

while True:
    elapsed = time.time() - start_time
    oxygen_left = max(0, total_oxygen - elapsed)

    if oxygen_left <= 0 and not final_question_mode:
        final_question_mode = True
        print("\n⚠️ Oxygen running low! This is your final question!")

    clear_screen()

    # show shipwreck message for last event if it was dive_for_treasure after screen clear
    if shipwreck_message:
        print(shipwreck_message)
        print()
        shipwreck_message = ""  # reset after showing

    # show outcome message for last event after screen clear
    if last_result:
        print(last_result)

    # show time and depth at top
    print(f"\n🕒 Oxygen left: {format_time(oxygen_left)} | 🌊 Depth {depth}")
    if final_question_mode:
        print("\n🌊 Final Question:")

    print("\nA new challenge appears...")

    correct, shipwreck_message = run_event()

    if correct:
        last_result = "✅ Correct!"
    else:
        last_result = "❌ Wrong! You lose oxygen."
        start_time -= oxygen_penalty

    if final_question_mode:
        print(f"\n{last_result}")
        print("\n⏳ Time's up! Your dive is over.")
        break

    depth += 1

print(f"\n🏁 Final Depth: {depth}")
save_score(player, depth)
show_leaderboard()