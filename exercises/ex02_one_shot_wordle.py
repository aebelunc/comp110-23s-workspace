"""EX02 - One Shot Wordle"""
__author__= "730621434"

#secret word variable (made constant)
SECRET: str = "python"
#Input for game start
guess: str = input(f"What is your {len(SECRET)}-letter guess? ")
#Variables for colored boxes
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
resulting_emoji = ""
#index set to 0 for counting
idx = 0
#alternate index for yellow boxes (same character exists in the wrong spot)
alt_idx = 0
#boolean statement for the alt index while loop
chr_exists: bool = False
#boolean for the original while loop or the entirety of the loop
playing: bool = True
#beginning of while statement loop 
while playing:
    #test to see if the indexes are the same length
    if len(guess) != len(SECRET):
        #input if the indexes are not the same length
        guess = str(input(f"That was not {len(SECRET)} letters! Try again: "))
    #while loop for when index lengths are ==
    while idx < len(SECRET):
        #test for if character indices match in the same spot
        if guess[idx] == SECRET[idx]:
            resulting_emoji += GREEN_BOX
        #for if they are not equal or do not match the spot in the index
        else:
            #while loop for the alternate index variable tests
            while alt_idx < len(SECRET) and not chr_exists:
                #test for if alt index == guess index setting our boolean variable to true
                if SECRET[alt_idx] == guess[idx]:
                    chr_exists = True
                #if not alt index variable counts up one
                else:
                    alt_idx += 1
            #tests if the index in guess is just in the secret word, if so the yellow box is concatinated
            if guess[idx] in SECRET:
                resulting_emoji += YELLOW_BOX
            else:
            #if not the white box signifies the letter in the index is not apart of the secret word
                resulting_emoji += WHITE_BOX
        idx += 1
    #print statement for after the index while loop completes
    print(resulting_emoji)
    #if the guess is the same as the secret word 
    if guess == SECRET: 
        print("Woo! You got it! ")
            #so the loop ends after correct guess
        playing = False
    #if the guess is wrong it exits out and tells you to play again
    else:
        print("Not quite. Play again soon! ")
        playing = False