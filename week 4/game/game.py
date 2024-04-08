import random

#Main loop keep asking for a level until a valid one is given
def main ():

    while True:
        try:
            level = ask_level()
        except TypeError:
            pass
        else:
            play_game(level)
            break

#Makes sure that the level is above 0 and is a integer and the returns the level.
def ask_level():

    level = input("level: ")

    if level.isdigit():
        level = int(level)
    else:
        raise TypeError

    if level < 0 or level == 0:
        raise TypeError

    return level

#Generates a random number with randint and then ask the user for a valid input, then its prints a hint about the guess.
def play_game(n):
    number = random.randint(1, n)

    while True:
        try:
            guess = input("Guess: ")

            if guess.isdigit():
                guess = int(guess)

            if guess < 0 or guess == 0:
                raise TypeError

        except TypeError:
            pass

        else:

            guess = int(guess)
            if guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
            else:
                print("Just right!")
                break


main()
