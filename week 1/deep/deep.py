#We define a main fuction that contains the main part of the program.

def main():
    #We take user input with input function and store it.
    response = input("What is the Answer to the Great Question of Life, the Universe, and Everything? \n")

    #We call the_answer function.
    the_answer(response)

    #we define the_Answer checks if any of the conditions it's true and print yes, otherwise prints no
def the_answer(input):
    input = input.strip().casefold()
    if input == "42" or input == "forty two" or input == "forty-two":
        print("yes")
    else: print("no")

    #Calling the main function
main()


