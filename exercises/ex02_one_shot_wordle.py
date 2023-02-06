"""EX02 - One-Shot Wordle - One shot at guessing secret word."""
__author__ = "730571588"

SECRET: str = "python"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

display: str = ""


guess: str = input("What is your 6-letter guess? ")
playing: bool = True 

while playing:
    if guess == SECRET: 
        display = GREEN_BOX * len(SECRET)
        print(display)
        print("Woo! You got it!") 
        playing = False
    else:
        if len(guess) != len(SECRET):
            guess = input(f"That was not {len(SECRET)} letters! Try again: ")
        else:
            i: int = 0
            while i < len(SECRET):
                if SECRET[i] == guess[i]:
                    display = display + GREEN_BOX
                else:
                    idx: int = 0
                    in_word: bool = False
                    while idx < len(SECRET):
                        if guess[i] == SECRET[idx]:
                            in_word = True
                        idx = idx + 1
                    if in_word:
                        display = display + YELLOW_BOX
                    else:
                        display = display + WHITE_BOX
                i = i + 1
            print(display)
            print("Not quite. Play again soon!")  
            playing = False