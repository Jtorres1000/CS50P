#Import Fliget class from pyfliget

from pyfiglet import Figlet

#import system and random modules
import sys, random

def main():

    check_input()

#Checks whether sys.argv has input or not, and makes sure that the input is written correctly.
def check_input():

    if len(sys.argv) == 1:
            print_random()

    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
            print_font()
    else:
        sys.exit("Invalid usage")

#Choose a random font from the font_list and uses it to print the input.
def print_random():

    fliget = Figlet()

    font_list = fliget.getFonts()
    fliget.setFont(font=f"{random.choice(font_list)}")
    string = input("input:\n")
    print(fliget.renderText(string))

#Checks if the font name given by the user is in font_list and uses it to print the message otherwise it exits.
def print_font():

    fliget = Figlet()
    font_list = fliget.getFonts()

    if sys.argv[2] in font_list:
        fliget.setFont(font=f"{sys.argv[2]}")
        string = input("input:\n")
        print(fliget.renderText(string))
    else:
        sys.exit("Invalid usage")


main()
