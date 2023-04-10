"""EX02 - Wordle."""
__author__ = "730621434"

def main() -> None:
    """The entrypoint of the program and main game loop."""
    # variables for the main().
    SECRET: str = "codes"
    guess: str = ""
    # made the turns a varibale so I could track the amount of turns you take in the game.
    turn: int = 1
    # while loop for our game. 
    while turn <= 6:
        # shows the amount of turns taken in the game. 
        print(f"=== Turn {turn}/6 ===")
        # made guess a variable equal to the input_guess def, calling it to make sure the guess has the right characters.
        guess = input_guess(len(SECRET))
        # added a guess_emoji variable to track the guesses index for matches to the secret word, also, this helps for the emojis to not interfere with the actual guess.
        guess_emoji = emojified(guess, SECRET)
        print(guess_emoji)
        if guess == SECRET:
            print(f"You won in {turn}/6 turns!")
            return
        # adding one to the turn after each loop.
        turn += 1
    # for when the guesses is up and you lose the game.
    print("x/6 - Sorry, try again tomorrow!")
# def for checking for indexes of the guessed word for matches.
def contains_char(str_search: str, onechar_search: str, ) -> bool:
    """Tests to see if string two's character is in the first string."""
    assert len(onechar_search) == 1
    idx = 0
    while idx < len(str_search):
        if str_search[idx] == onechar_search:
            return(True)
        idx += 1
    return(False)
# def for adding emojis to matching, non matching, and outright incorrect letters.
def emojified(guess: str, SECRET: str) -> str:
    """Adding emojies that return when conditions in guess and SECRET are evaluated"""
    assert len(guess) == len(SECRET)
    # variables for the emojis
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # added a search variable that is an empty string for the emojis to concatinate to.
    search: str = ""
    idx = 0
    alt_idx = 0
    # while loop for checking for the indicies.
    while idx < len(guess):
        if guess[idx] == SECRET[idx]:
            search += GREEN_BOX
            alt_idx += 1
        else:
            if contains_char(SECRET, guess[idx]):
                search += YELLOW_BOX
            else:
                search += WHITE_BOX
        idx += 1
    # returns the search variable which includes the colored boxes.
    return(search)
# def for the inputed guessed word and to check if it has the correct character length. 
def input_guess(expected_length: int) -> str:
    """Definition to input the guess to the game"""
    # starts off the game here with the input asking for the correct length of characters word.
    guess = input(f'Enter a {expected_length} character word: ')
    # while loop for checking the length of the guess
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again:")
    else:
        return guess
# so the game is playable!
if __name__ == "__main__":
    main()