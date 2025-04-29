import sys
import random
import time

def display_score(score):
    # Display score
    print(f"[Score: {score}] ", end="")

def pause(seconds=1):
    # Pause for seconds
    time.sleep(seconds)

def fight_monster(score):
    # Fight monster
    display_score(score)
    fight_choice = input("Do you want to fight the monster or run away? (fight/run) ").lower()
    if fight_choice == "fight":
        outcome = random.choice(["win", "lose"])
        if outcome == "win":
            print("You defeated the monster!")
            score += 20
        else:
            print("The monster defeated you!")
            score -= 10
    else:
        print("You ran away.")
        score -= 5
    return score

def story(score=0):
    # Start the story
    print("\nYou are in a green zone full of trees and flowers. You are a mid-age male.")
    print("The sun is shining and the birds are singing.")
    pause(2)
    print("You are walking in the forest and you see a big tree.")
    print("You go to the tree and you see a door.")
    print("You open the door and find a woman saying:")
    print("'I heard you're the new warrior of the forest.'")
    pause(2)
    print("'The forbidden creature is going to destroy the forest. You should stop him.'")

    display_score(score)
    accept = input("Do you accept the mission? (yes/no) ").lower()
    if accept == "yes":
        print("You are now a warrior.")
        score += 10
    else:
        print("You continue by force.")
        score -= 5

    pause(2)
    print("\nYou see a big tree again.")
    print("You go to the tree and you see a door.")
    display_score(score)
    open_door = input("Do you want to open the door? (yes/no) ").lower()
    if open_door == "yes":
        print("You open the door and see a big monster.")
        pause(2)
        score = fight_monster(score)
    else:
        print("The Dragon attacked you. (You Lost)")
        score -= 10

    if score < 0:
        # Game over
        print("Your score is too low... Game Over!")
        sys.exit()

    playagain(score)

def playagain(score):
    # Ask to play again
    display_score(score)
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "yes":
        story(score)
    else:
        print(f"Thanks for playing! Your final score is: {score}")
        sys.exit()

# Start the story
story()
