#We define a main fuction that contains the main part of the program.

def main():
    #We take user input with input function and store it.
    expression = input("Enter the expression:\n")

    #We call math function.
    math(expression)

    #We define math function that divides the user input into parts and assigns each individual value to a different variable, then checks what type of operation it was when it checked and prints the result of that operation.
def math(input):
    x, y, z = input.split(" ")
    if y == "+":
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    else: print(float(x) / float(z))

    #Calling the main function
main()
