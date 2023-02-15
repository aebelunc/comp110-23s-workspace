"""EX02 - One Shot Wordle"""
__author__= "730621434"

#secret word variable (made constant)
SECRET: str = "python"
#Input for game start
guess: str = input(f"What is your {len(SECRET)}-letter guess? ")
#variable for while statement
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
resulting_emoji = ""
idx = 0
alt_idx = 0
chr_exists: bool = False
playing: bool = True
#beginning of while statement loop 
while playing:
    if len(guess) != len(SECRET):
        guess = str(input(f"That was not {len(SECRET)} letters! Try again: "))
    while idx < len(SECRET):
        if guess[idx] == SECRET[idx]:
            resulting_emoji += GREEN_BOX
        else:
            while alt_idx < len(SECRET) and not chr_exists:
                if SECRET[alt_idx] == guess[idx]:
                    chr_exists = True
                else:
                    alt_idx += 1
            if guess[idx] in SECRET:
                resulting_emoji += YELLOW_BOX
            else:
                resulting_emoji += WHITE_BOX
        idx += 1
    print(resulting_emoji)
    if guess == SECRET: 
        print("Woo! You got it! ")
            #so the loop ends after correct guess
        playing = False
    else:
        print("Not quite. Play again soon! ")
        playing = False