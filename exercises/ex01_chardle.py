"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730571588"

five_word: str = input("Enter a 5-character word: ")

if len(five_word) != 5:
    print("Error: Word must contain 5 characters")
    exit() 

single_letter: str = input("Enter a single character: ")

if len(single_letter) != 1:
    print("Error: Character must be a single character.")
    exit() 

print("Searching for " + single_letter + " in " + five_word)

count: int = 0

if five_word[0] == single_letter:
    print(single_letter + " found at index 0")
    count = count + 1
if five_word[1] == single_letter:
    print(single_letter + " found at index 1")
    count = count + 1
if five_word[2] == single_letter:
    print(single_letter + " found at index 2")
    count = count + 1
if five_word[3] == single_letter:
    print(single_letter + " found at index 3")
    count = count + 1
if five_word[4] == single_letter:
    print(single_letter + " found at index 4")
    count = count + 1

if count == 1:
    print(str(count) + " instance of " + single_letter + " found in " + five_word)
else:
    if count != 0:
        print(str(count) + " instances of " + single_letter + " found in " + five_word)
    else:
        print("No instances of " + single_letter + " found in " + five_word)