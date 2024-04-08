#We define a main fuction that contains the main part of the program.
def main():
    #We take user input with input function and store it.
    user_input = input("Input:\n")

    #We call print the return of the not_vowels function.
    print(not_vowels(user_input))

    #defining the not_vowels function.
def not_vowels(word):
    #We create a table with maketrans, it takes 3 parameters the last one is the characters we wanted to eliminate
    table = str.maketrans("", "", "aeiouAEIOU")

    #them we return the user input translate with the table.
    return word.translate(table)

    #calling main function
main()
