"""EX03 - Structured Wordle"""
__author__ = "730571588"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char(any_length: str, one_character: str) -> bool:
    """Outputs bool if one_character is found at any index of any_length."""
    assert len(one_character) == 1

    i: int = 0
    while i < len(any_length):
        if one_character == any_length[i]:
            return True 
        i += 1
    return False 


def emojified(guess: str, secret: str) -> str:
    """Output emojis that color codifies."""
    assert len(guess) == len(secret)
    display: str = ""
    
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            display = display + GREEN_BOX
        elif contains_char(secret, guess[i]): 
            display = display + YELLOW_BOX
        else:
            display = display + WHITE_BOX
        i += 1
    return display


def input_guess(expected_length: int) -> str:
    """Output a string and provide guess for expected_length"""
    length: str = input("Enter a " + str(expected_length)+ " character word: ")
    while len(length) != expected_length:
        length = input("That wasn't " + str(expected_length)+ " chars! Try again: ") 
    else:
        return length


def main() -> None:
    """The entrypoint of the program and main game loop"""
    secret: str = "codes"
    playing: bool = True
    turn: int = 0

    while playing:
        turn += 1
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(5)
        print(emojified(guess, secret))
        if guess == secret:
            playing = False 
            print(f"=== Turn {turn}/6 ===")
        elif turn > 5:
            playing = False
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
