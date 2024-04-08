#We define a main fuction that contains the main part of the program.

def main():
    #We take user input with input function and store it.
    word = input("Enter a emoji to replace: \n")

    #We call the faces function.
    faces(word)

    #we define faces input it replaces the string :) or :( with their equivalent in codepoints in order to get the actual emoji.
def faces(input):

    print(input.replace(":)", "\U0001F642").replace(":(", "\U0001F641"))

    #Calling the main function
main()


