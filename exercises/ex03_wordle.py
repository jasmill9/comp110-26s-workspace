"""EX03 - wordle - The REAL wordle."""

__author__ = "730765442"


def input_guess(length: int) -> str:
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        # Repeat the prompt as long as the length is incorrect
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Finding charecter and length matches"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        # return true if the character is found at the current index
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(first_guess: str, sec_guess: str) -> str:
    """revealing correct and incorrect guesses"""
    assert len(first_guess) == len(sec_guess)
    # checks equal strings length
    WHITE_BOX: str = "\U00002b1c"
    # not in word
    GREEN_BOX: str = "\U0001f7e9"
    # in word, in the spot
    YELLOW_BOX: str = "\U0001f7e8"
    # in word, different spot
    result: str = ""
    index: int = 0
    while index < len(sec_guess):
        # Loop through each index of the guess to determine the correct color box
        if first_guess[index] == sec_guess[index]:
            result += GREEN_BOX
        elif contains_char(sec_guess, first_guess[index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        index += 1
    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    max_turns: int = 6
    won: bool = False
    while turn <= max_turns and not won:
        # run the game until the user wins or runs out of turns
        print(f"=== Turn {turn}/6===")
        guess: str = input_guess(len(secret))
        print(emojified(secret, guess))
        if guess == secret:
            won = True
        else:
            turn += 1
        if won:
            print(f"You won in {turn}/6 turns!")
        else:
            print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main("codes")
