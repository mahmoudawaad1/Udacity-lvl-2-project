import sys
import random
import time

# Random weather
weather_choice = ["sunny", "rainy", "stormy"]
weather = random.choice(weather_choice)

def display_score(score):
    print(f"[Score: {score}] ", end="")

def pause(seconds=1):
    time.sleep(seconds)

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower().strip()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}.")

def fight_monster(score):
    display_score(score)
    fight_choice = get_valid_input("Do you want to fight the monster or run away? (fight/run) ", ["fight", "run"])
    if fight_choice == "fight":
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            print("You bravely slay the monster!")
            score += 10
        else:
            print("The monster overpowered you!")
            score -= 10
    else:
        print("You ran away and lost honor.")
        score -= 10
    return score

def escape_dragon(score):
    print("You see two escape paths: the forest or the jungle.")
    display_score(score)
    path = get_valid_input("Where do you run? (forest/jungle) ", ["forest", "jungle"])
    if path == "forest":
        print("You trip over a root, but survive.")
        score -= 5
    elif path == "jungle":
        print("You hide in thick vines and the dragon passes.")
        score += 10
    return score

def explore_forest(score):
    print("\nYou find a fork in the road.")
    print("To the left: an eerie cave. To the right: a glowing waterfall.")
    display_score(score)
    choice = get_valid_input("Which way do you go? (cave/waterfall) ", ["cave", "waterfall"])
    if choice == "cave":
        print("A goblin attacks you in the dark.")
        score -= 10
    elif choice == "waterfall":
        print("You find a healing herb behind the falls.")
        score += 10
    return score

def meet_traveler(score):
    print("\nA hooded traveler approaches you.")
    print("He offers a map or a sword.")
    display_score(score)
    gift = get_valid_input("What do you take? (map/sword) ", ["map", "sword"])
    if gift == "map":
        print("The map reveals a secret route.")
        score += 10
    elif gift == "sword":
        print("The sword is cursed! You feel weak.")
        score -= 10
    return score

def ancient_ruins(score):
    print("\nYou discover ancient ruins with inscriptions.")
    display_score(score)
    choice = get_valid_input("Do you read the inscriptions or move on? (read/move) ", ["read", "move"])
    if choice == "read":
        print("You unlock ancient wisdom. You gain clarity.")
        score += 10
    elif choice == "move":
        print("You miss out on powerful knowledge.")
        score -= 10
    return score

def story(score=0):
    print(f"\n🌳 You are in a vast forest, {weather} weather.")
    pause(2)
    print("You approach a mystical tree with a door.")
    pause(1)
    print("Inside stands a mysterious woman:\n'I heard you're the new warrior.'")
    pause(2)
    print("'The forbidden creature will destroy us all unless you stop him.'")

    display_score(score)
    accept = get_valid_input("Do you accept the mission? (yes/no) ", ["yes", "no"])
    if accept == "yes":
        print("You accept and gain courage.")
        score += 10
    else:
        print("Mate why do you refuse? :/ you will continue by force anyway and I will take 10 points from you too.")
        score -= 10

    pause(2)
    print("\nAfter a while, you open another glowing door...")
    print("A massive dragon roars from inside!")
    display_score(score)
    open_door = get_valid_input("Do you want to enter or run? (enter/run) ", ["enter", "run"])
    if open_door == "enter":
        score = fight_monster(score)
    else:
        print("The dragon bursts through the door and chases you!")
        score -= 10
        score = escape_dragon(score)

    pause(2)
    score = explore_forest(score)
    pause(2)
    score = meet_traveler(score)
    pause(2)
    score = ancient_ruins(score)

    print("\nYou approach the Forbidden Creature's lair.")
    print("You feel the weight of your journey.")
    display_score(score)
    final_choice = get_valid_input("Do you enter the lair or camp for the night? (enter/camp) ", ["enter", "camp"])
    if final_choice == "enter":
        print("You face the beast in an epic battle...")
        outcome = random.choice(["victory", "defeat"])
        if outcome == "victory":
            print("You have saved the forest! 🌟")
            score += 20
        else:
            print("You fought bravely but fell. The forest mourns.")
            score -= 20
    else:
        print("The beast attacked your camp at night. You were unprepared!")
        score -= 10
        pause(2)
        print("\nYou wake up to flames and roaring nearby!")
        print("You must escape quickly! What do you do?")
        display_score(score)
        escape_option = get_valid_input("Hide in bushes, climb a tree, or panic fight? (hide/climb/fight) ", ["hide", "climb", "fight"])
        if escape_option == "hide":
            print("You hide under the bush. The dragon flies past. You survive!")
            score -= 5
        elif escape_option == "climb":
            print("You climb a tree. The dragon sees you but ignores you. You're lucky!")
            score -= 5
        elif escape_option == "fight":
            print("You swing your weapon blindly. You wound the beast, but take damage too.")
            score -= 10

    if score < -30:
        print("Your score is too low... You have failed the forest.")
        sys.exit()

    playagain(score)

def playagain(score):
    display_score(score)
    again = get_valid_input("Do you want to continue your journey? (yes/no) ", ["yes", "no"])
    if again == "yes":
        story(score)
    else:
        print(f"Thanks for playing! Final Score: {score}")
        sys.exit()

def main():
    story()

if __name__ == "__main__":
    main()
