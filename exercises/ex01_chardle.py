"""EX01 - Chardle."""
__author__ = "730621434"

word_user: str = input("Enter a 5-character word: ")
if (len(word_user) != 5):
    print("Error: Word must have 5 characters")
    exit()
character_user: str = input("Enter a single character: ")
if (len(character_user) !=1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + character_user + " in " + word_user + " ")
if (character_user == word_user [0]): 
    print( character_user + " found at index 0")
if (character_user == word_user [1]):
    print( character_user + " found at index 1")
if (character_user == word_user [2]):
    print(character_user + " found at index 2" )
if (character_user == word_user [3]):
    print(character_user + " found at index 3")
if (character_user == word_user [4]):
    print(character_user + " found at index 4")
matching_index = sum(1 if x == character_user else 0 for x in word_user)
if (matching_index == 0):
    print("No instances of " + character_user + " found in " + word_user)
if (matching_index == 1):
    print(matching_index, "instance of " + character_user + " found in " + word_user)
if (matching_index > 1): 
    print(matching_index, "instances of " + character_user + " found in " + word_user)

    


