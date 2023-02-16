"""EX02 - One Shot Wordle."""
__author__ = "730621434"

# secret word variable (made constant)
SECRET: str = "python"
# Input for game start
guess: str = input(f"What is your {len(SECRET)}-letter guess? ")
# Variables for colored boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
resulting_emoji = ""
# index set to 0 for counting
idx = 0
# boolean for the original while loop or the entirety of the loop
playing: bool = True
# boolean for testing the alternate indices
chr_exists: bool = False
# for counting the alternate indices
alt_idx = 0
# beginning of while statement loop 
while playing:
    # test to see if the indexes are the same length
    if len(guess) != len(SECRET):
        # input if the indexes are not the same length
        guess = str(input(f"That was not {len(SECRET)} letters! Try again: "))
    # while loop for when index lengths are equal
    else:
        while idx < len(SECRET):
            # test for if character indices match in the same spot
            if guess[idx] == SECRET[idx]:
                resulting_emoji += GREEN_BOX
            # for if they are not equal or do not match the spot in the index
            else:
                # while loop for the alternate index variable tests
                while not chr_exists and alt_idx < len(SECRET):
                    # test for if alt index equals guess index setting our boolean variable to true
                    if SECRET[alt_idx] == guess[idx]:
                        chr_exists = True
                    else:
                        # to increment the alternate index variable 
                        alt_idx += 1
                # tests to see if the current index is in the SECRET making the boolean true
                if guess[idx] in SECRET:
                    resulting_emoji += YELLOW_BOX
                # put at the end so the white boxes don't overshadow the yellow ones like they would if put in the else block after the intial test
                else:
                    resulting_emoji += WHITE_BOX
        # adding one to the index variable to make sure count is correct, print statement for after the index while loop completes, and playing set to False so there isn't an infinite loop
            idx += 1
        print(resulting_emoji)
        playing = False
# if the guess is the same as the secret word 
if guess == SECRET: 
    print("Woo! You got it! ")
    # so the loop ends after correct guess
    playing = False
# if the guess is wrong it exits out and tells you to play again
else:
    print("Not quite. Play again soon! ")
playing = False