import sys
import csv
from tabulate import tabulate

#Main function, prints out the outpout of the functions and handle errors in user input.
def main ():

    try:
        handle_arg()
        print(style_table(open_file()))

    except TypeError:
        sys.exit("Too few command-line arguments")
    except ValueError:
        sys.exit("Too many command-line arguments")
    except NameError:
        sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("File does not exist")

#Handle_arg, makes sure that there's not error with the user input.
def handle_arg():

    if len(sys.argv) == 1:
        raise TypeError
    if len(sys.argv) > 2:
        raise ValueError
    elif not sys.argv[1].endswith(".csv"):
        raise NameError

#opens the csv file and appends each row in a table list.

def open_file():

    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        table = []

        for row in reader:
            table.append(row)

        return table

#Returns a styled table.
def style_table(table):

    return tabulate(table, headers="firstrow", tablefmt="grid")

if __name__ == "__main__":
    main()
