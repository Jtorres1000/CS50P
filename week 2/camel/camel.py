
#We define a main fuction that contains the main part of the program.
def main():
    #We take user input with input function and store it.
    camel = input("camelCase:\n")

    #We call the snake_case function.
    snake_case(camel)

    #defining the snake_case function.
def snake_case(word):
    #for each letter we will check if it is uppercase, if that is the case "_" is printed plus the lowercase letter, otherwise it is printed normally.
    for letter in word:
        if letter.isupper():
            print("_" + letter.casefold(), end="")
        else: print(letter, end="")

    #calling main function.
main()
