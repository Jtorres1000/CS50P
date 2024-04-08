#We define a main fuction that contains the main part of the program.

def main():
    #We take user input with input function and store it.
    greeting = input("Enter a greeting \n")

    #We call the_answer function.
    newman(greeting)

    #we define newman function checks if it starts with hello and print $0 or with h and prints $20, otherwise it prints $100
def newman(input):

    input = input.strip().casefold()
    
    if input.startswith("hello"):
        print("$0")
    elif input.startswith("h"):
        print("$20")
    else: print("$100")

    #Calling the main function
main()


