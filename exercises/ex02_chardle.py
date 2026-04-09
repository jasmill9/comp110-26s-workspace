"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730765442"


def main() -> None:
    # main function controls and guides the flow of the program like a step by step
    word: str = input_word()
    # step 1: input_word is called program runs at lines 14-21
    letter: str = input_letter()
    # step 2: input_letter is called program runs at line 25-31
    contains_char(word, letter)


# final step contains_char is called to check for matching input: 34-66


def input_word() -> str:
    """prompting user to enter a 5-letter word function"""
    word: str = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        # exit function ensures the program stops running after an invalid input
    else:
        return word


def input_letter() -> str:
    """prompting user to enter a single letter"""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    """Checking if input matches"""
    print("Searching for " + letter + " in " + word)
    count: int = 0
    # CL10: Variable Declaration:
    # <name> (count): <type> (int) = assignment (0)
    if word[0] == letter:
        print("No instances of " + letter + " found in " + word)
        count = count + 1
        # reassigning count in this instance to the value of 1
        # then print the entered letter (i.e. h) + found at index 0
        # finally add 1 to the count of total successes, or
    if word[1] == letter:
        print((letter) + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print((letter) + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print((letter) + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print((letter) + " found at index 4")
        count = count + 1

    if count == 0:
        print("No instances of " + (letter) + " found in " + (word))
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


if __name__ == "__main__":
    main()
