
#We define a main fuction that contains the main part of the program.

def main():
    #We take user input with input function and store it.
    word = input("Enter a word: \n")

    #We call the indoor function.
    indoor(word)

    #defining the indoor function with input argument default value being indoor to handle empty inputs.
def indoor(input="INDOOR"):
    print(input.casefold())

    #calling main function.
main()
