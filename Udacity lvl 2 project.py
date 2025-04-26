import sys

def display_score(score):
    print(f"[Score: {score}] ", end="")

def playagain(score):
    display_score(score)
    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again == "yes":
        story(score)
    else:
        print(f"Thanks for playing! Your final score is: {score}")
        sys.exit()

def story(score=0):
    print("\nYou are in a green zone full of trees and flowers. You are a mid-age male.")
    print("The sun is shining and the birds are singing.")
    print("You are walking in the forest and you see a big tree.")
    print("You go to the tree and you see a door.")
    print("You open the door and find a woman saying:")
    print("'I heard you're the new warrior of the forest.'")
    print("'The forbidden creature is going to destroy the forest. You should stop him.'")

    display_score(score)
    accept = input("Do you accept the mission? (yes/no) ").lower()
    print("\n")
    if accept == "yes":
        print("You are now a warrior of the forest.")
        score += 10
    else:
        print("Mate, why do you refuse it? You will continue by force now xD")
        print("You are now the warrior of the forest.")
        score -= 5

    print("\nYou are now in the forest and you see a big tree again.")
    print("You go to the tree and you see a door.")
    display_score(score)
    open_door = input("Do you want to open the door? (yes/no) ").lower()
    print("\n")
    if open_door == "yes":
        print("You open the door and you see a big monster.")
        print("The monster is very big and scary.")
        print("You are now in a fight with the monster.")
        display_score(score)
        fight1 = input("Do you want to fight the monster or run away? (fight/run) ").lower()
        print("\n")
        if fight1 == "fight":
            print("You really thought you could kill such a monster with bare hands? (You Lost)")
            score -= 10
            playagain(score)
        else:
            print("You run away and you see another big tree.")
            print("You go to the tree and you see a door.")
            display_score(score)
            open_door = input("Do you open the door? (yes/no) ").lower()
            print("\n")
            if open_door == "yes":
                print("You see a guy selling magical weapons.")
                print("He says, 'Would you like to buy a magical sword?'")
                display_score(score)
                buy = input("Do you want to buy the sword? (yes/no) ").lower()
                print("\n")
                if buy == "yes":
                    print("You buy the sword and you see a big monster.")
                    print("The monster is very big and scary.")
                    print("You are now in a fight with the monster.")
                    display_score(score)
                    fight2 = input("Do you want to fight the monster or run away? (fight/run) ").lower()
                    print("\n")
                    if fight2 == "fight":
                        print("You used your magical sword and killed the monster!")
                        print("You are now the hero of the forest!")
                        score += 20
                        playagain(score)
                    else:
                        print("The monster attacked you while you were running away. (You Lost)")
                        score -= 10
                        playagain(score)
                else:
                    print("You didn't buy the sword.")
                    print("You saw a big and scary monster, and he killed you. (You Lost)")
                    score -= 10
                    playagain(score)
            else:
                print("The Dragon opened the door and attacked you. (You Lost)")
                score -= 10
                playagain(score)
    else:
        print("The Dragon opened the door and attacked you. (You Lost)")
        score -= 10
        playagain(score)

# Start the story
story()
