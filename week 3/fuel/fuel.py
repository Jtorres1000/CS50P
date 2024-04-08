#We define a main fuction that contains the main part of the program.

def main():

    #We call the catch_errors function.
    catch_errors()

    #Catch_errors function has a while loop to keep asking for a fraction until a valid input is given.
def catch_errors():

    while True:
        try:
            value = input("Fraction:\n")
            fuel(value)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        else:
            break

#Fuel function calls int_list to take the user input and convert it to a list of integer values, then evaluates the division to see what % it returns, deduces if any errors may occur before doing any calculations, and raises the error type.
def fuel(input):

    str_list = input.split("/")

    lst = list(map(lambda x: int(x), str_list))

    if lst[0] > lst[1]:
        raise ValueError
    if lst[1] == 0:
        raise ZeroDivisionError

    division = lst[0] / lst[1]

    if division >= 0.99:
        print("F")
    elif division <= 0.01:
        print("E")
    else:
        print(f"{round(division * 100)}%")

    #Calling the main function
main()


