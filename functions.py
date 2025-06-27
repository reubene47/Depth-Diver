import time
import random
import csv
import os

# clear the terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# format time
def format_time(seconds):
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins}:{secs:02}"

# save score to scores.csv
def save_score(name, depth):
    file = "scores.csv"
    exists = os.path.exists(file)
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow(["Name", "Depth"])
        writer.writerow([name, depth])

# display leaderboard filtered for top 5 scores
def show_leaderboard():
    file = "scores.csv"
    if not os.path.exists(file):
        print("\nNo scores yet.")
        return
    with open(file, "r") as f:
        reader = csv.reader(f)
        next(reader)
        scores = sorted(reader, key=lambda r: int(r[1]), reverse=True)
        print("\n🏆 Top Divers:")
        for i, (name, depth) in enumerate(scores[:5], 1):
            print(f"{i}. {name} - Depth {depth}")

# for all inputs to ensure they are lowercase and stripped
def ask(prompt):
    return input(prompt).strip().lower()

# odd one out of 5 sea creatures
def odd_one_out():
    sea_animals = ["🐠", "🐟", "🐬", "🦑", "🦐", "🦞", "🐡", "🐙"]
    correct_animal = random.choice(sea_animals)
    odd_animal = random.choice([a for a in sea_animals if a != correct_animal])
    items = [correct_animal] * 4 + [odd_animal]
    random.shuffle(items)

    print("\nWhich sea animal is the odd one out?")
    for i, item in enumerate(items, 1):
        print(f"{i}) {item}")
    answer = ask("Your answer (1-5): ")
    if not answer.isdigit() or int(answer) not in [1, 2, 3, 4, 5]:
        return False
    return items[int(answer) - 1] == odd_animal

# quick choice between recyclable items and sea creatures
def quick_choice():
    recyclable = ["Plastic Bottle", "Tin Can", "Glass Bottle", "Old Shoe"]
    creatures = ["Jellyfish", "Crab", "Fish", "Octopus"]
    task = random.choice(["grab", "avoid"])
    correct_set = set(recyclable if task == "grab" else creatures)
    items = random.sample(list(correct_set), 2)
    items += [random.choice(list(set(recyclable + creatures) - correct_set))]
    random.shuffle(items)
    print(f"\nQuick! {'Grab a recyclable' if task == 'grab' else 'Avoid a sea creature'}")
    for i, item in enumerate(items, 1):
        print(f"{i}) {item}")
    answer = ask("Your answer (1-3): ")
    if not answer.isdigit() or int(answer) not in [1, 2, 3]:
        return False
    choice = items[int(answer)-1]
    return (choice in correct_set) if task == "grab" else (choice not in correct_set)

# simple math problems with sea animals as units
def simple_math():
    sea_animals = ["🐠", "🐟", "🐬", "🦑", "🦐", "🦞", "🐡", "🐙"]
    a = random.randint(10, 30)
    b = random.randint(1, 9)
    a, b = max(a, b), min(a, b)
    animal = random.choice(sea_animals)
    correct = a - b
    print(f"\nSolve: {a} {animal} - {b} {animal} = ?")
    answer = ask("Your answer: ")
    return answer.isdigit() and int(answer) == correct

# dive for treasure near a shipwreck with a 50% chance of finding treasure
# and a 50% chance of encountering a sea creature, wasting time
def dive_for_treasure():
    sea_animals = ["shark 🦈", " large fish 🐟", "dolphin 🐬", "Squid 🦑", "lobster 🦞", "puffer fish 🐡", "octopus 🐙"]
    print("\nYou see something shiny near a shipwreck...")
    print("1) Dive for it")
    print("2) Swim past safely")
    choice = input("Choose 1 or 2: ").strip()

    if choice == "2":
        return True, "You swim past safely."
    elif choice == "1":
        outcome = random.choice(["treasure", "creature"])
        if outcome == "treasure":
            return True, "🏴‍☠️ You found a sunken ship and a chest full of gold!"
        else:
            animal = random.choice(sea_animals)
            return False, f"🐙 Oh no! A {animal} scared you away!"
    
    return False, "You hesitated too long..."

# pattern recognition using sea creatures, choose the creature that finishes the sequence
def pattern_recognition():
    sea_animals = ["🐠", "🐟", "🐬", "🦑", "🦐", "🦞", "🐡", "🐙"]
    a = random.choice(sea_animals)
    b = random.choice([x for x in sea_animals if x != a])

    # List of possible patterns (no keys!)
    pattern_options = [
        [a, b, a, b, a],
        [a, a, b, b, a],
        [a, b, b, a, b, b]
    ]

    full = random.choice(pattern_options)
    shown = full[:-1]
    next_item = full[-1]

    print(f"\nWhat comes next in this pattern?")
    print("Pattern:", " ".join(shown) + " ❓")

    # Multiple choice answers
    choices = [next_item]
    while len(choices) < 3:
        opt = random.choice(sea_animals)
        if opt not in choices:
            choices.append(opt)
    random.shuffle(choices)

    for i, opt in enumerate(choices, 1):
        print(f"{i}) {opt}")
    answer = input("Your answer (1-3): ").strip()
    return answer.isdigit() and int(answer) in [1, 2, 3] and choices[int(answer)-1] == next_item

# run a random event from the 5
def run_event():
    event = random.choice([
        odd_one_out,
        quick_choice,
        simple_math,
        dive_for_treasure,
        pattern_recognition
    ])

    if event == dive_for_treasure:
        return event()
    
    return event(), ""