"""EX06 - Choose Your Own Adventure."""
__author__: 730621434


SAD_FACE: str = "\U0001F615"
CRY_FACE: str = "\U0001F62D"
HAPPY_FACE: str = "\U0001F604"
CRAZY_FACE: str = "\U0001F92A"
DISSAPOINT: str = "\U0001F612"
DEAD: str = "\U0001F480"
BOAT: str = "\U0001F6A2	"

player: str = ""
points: int = 0


def main() -> None:
    """Def for the main function of the game."""
    global points
    global player
    points = 0
    greet()
    while True:
        points = 0
        print(f"You currently have {points} adventure points.")
        choice: str = input("Which character do you want to hang out with? goku or luffy or I don't like anime. ")
        
        if choice == "goku":
            print("You have chosen Goku! Get ready to save the world!")
            points = goku()
            print(f"\nYou now have {points} adventure points.")
        elif choice == "luffy":
            print(f"You have chosen Luffy! Get ready to set sail and find the One Piece! {BOAT}")
            points = luffy()
            print(f"\nYou now have {points} adventure points.")
        elif choice == "I don't like anime":
            print(f"Why are you even here! Leave at once, you finished with {points} adventure points.")
            return
        play_again = input("Do you want to play again? (yes or no) ")
        if play_again == "no":
            print(f"Thanks for playing, {player}! You finished with {points} adventure points.")
            return
        elif play_again == "yes":
            print("Starting over.....")
            continue
        else:
            print("Invalid choice, please try again.")

    
def greet() -> None:
    """Greet function for the beginning of the game."""
    global player
    print("Welcome! Have you ever wanted to adventure with your favorite anime characters? Well look no further and start now!")
    player = input("Enter your name: ")


def goku() -> None:
    """Function for when player selects goku."""
    global player
    global points
    print(f"{player}, you have chosen Goku. Get ready for an epic adventure!")

    # Option 1
    print("Goku needs to train his body to become stronger. Do you want to join him?")
    choice = input("Enter y for Yes or n for No: ")
    if choice == "y":
        print("Great! You join Goku in his training and get stronger. You gain 2 adventure points!")
        points += 2
    elif choice == "n":
        print("No worries, you can rest while Goku trains. You gain 1 adventure point.")
        points += 1
    else:
        print("Invalid input. You miss your chance to train with Goku.")

    # Option 2
    print("Goku hears about a powerful opponent that he wants to fight. Do you want to join him?")
    choice = input("Enter y for Yes or n for No: ")
    if choice == "y":
        print("Awesome! You and Goku face the opponent and come out victorious. You gain 2 adventure points!")
        points += 2
    elif choice == "n":
        print("No problem, you stay behind while Goku fights the opponent. You gain 1 adventure point.")
        points += 1
    else:
        print("Invalid input. You miss your chance to fight the opponent with Goku.")

    # Option 3
    print("Goku needs to find the Dragon Balls to save the world. Do you want to help him?")
    choice = input("Enter y for Yes or n for No: ")
    if choice == "y":
        print("Great teamwork! You and Goku find all the Dragon Balls and save the world. You gain 2 adventure points!")
        points += 2
    elif choice == "n":
        print("No worries, Goku can find the Dragon Balls on his own. You gain 1 adventure point.")
        points += 1
    else:
        print("Invalid input. You miss your chance to help Goku find the Dragon Balls.")
        print(f"{player}, you have completed the Goku adventure with {points} adventure points!")
    if points == 6:
        print(f"Goku let's you make a wish with the Dragon Balls! Make your wish warrior! {HAPPY_FACE}")
    return points


def luffy() -> int:
    """Function for when the player chooses Luffy."""
    global player
    global points
    
    # Option 1
    print(f"{player}, you find yourself on a deserted island with Luffy from One Piece!")
    print("Luffy invites you to join his crew and become a pirate. Do you accept?")
    choice: str = input("Enter y for Yes or n for No: ")
    if choice == "y":
        print("Great! You are now officially a member of the Straw Hat Pirates!")
        points += 2
    else:
        print("Oh no! Luffy is disappointed.")
        points += 1
    
    # Option 2
    print("Now that you're part of the crew, you need to learn how to fight. What style do you want to learn?")
    print("A) Haki")
    print("B) Rokushiki")
    print("C) Fishman Karate")
    choose: str = input("Enter A, B, or C: ")
    if choose == "A":
        print("You learn the ways of Haki and become a powerful warrior!")
        points += 3
    elif choose == "B":
        print("You learn the Rokushiki style and become an agile fighter!")
        points += 2
    elif choose == "C":
        print("You learn Fishman Karate and become a skilled underwater combatant!")
        points += 1
    
    # Option 3
    print("Oh no! Kaido has shown up to challenge you. Do you accept the battle?")
    choice: str = input("Enter y for yes and n for No: ")
    if choice == "y":
        print("Awesome! Your battle starts now.")
        if points >= 5:
            print(f"You and Kaido begin an amazing battle that will be remembered for ages as The Day the Beast Fell! because you win in striking fashion! {CRAZY_FACE}")
        else:
            print(f"It looks like your day as a Straw Hat comes to an end. Kaido proved too powerful and ended your life! {DEAD}")
    elif choice == "n":
        print(f"Luffy is disappointed in you but will always be your friend {SAD_FACE}. Luffy engages in battle and activates Gear 5! Kaido falls to his impressive power!")
    
    return points


if __name__ == "__main__":
    main()