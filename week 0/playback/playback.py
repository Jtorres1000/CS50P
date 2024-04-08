#We define a main fuction that contains the main part of the program.

def main():
    #We take user input with input function and store it.
    word = input("Enter a word: \n")
    #We call the playback function.
    playback(word)

    #defining the playback function with input argument default value being THIS IS A PLAYBACK to handle empty inputs.
def playback(input="THIS IS A PLAYBACK"):
    print(input.replace(" ", "..."))
    
    #Calling the main function.
main()

