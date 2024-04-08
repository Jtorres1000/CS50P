import sys
import csv

#Main function, handle errors in user input and calls the function that creates the new file.
def main ():

    try:
        handle_arg()
        write_file(change_dict(open_file()))

    except TypeError:
        sys.exit("Too few command-line arguments")
    except ValueError:
        sys.exit("Too many command-line arguments")
    except NameError:
        sys.exit("Not a CSV file")
    except FileNotFoundError:
        sys.exit("Could not read 1.csv")

#Handle_arg, makes sure that there's not error with the user input.
def handle_arg():

    if len(sys.argv) < 2:
        raise TypeError
    if len(sys.argv) > 3:
        raise ValueError
    if not sys.argv[1].endswith(".csv"):
        raise NameError

#open_file opens the file and makes a dict then modify it spliting the value of name in two parts and returns it.
def open_file():
    students = []

    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)

        for row in reader:
            students.append({"name": row["name"].split(", "), "house": row["house"]})

    return students

#change_dict takes the dict with the names split and makes a new one adding first, and last key pair values.
def change_dict(list_dict):

    new_list = []

    for dict in list_dict:

        new_dict = {'first':'', 'last': '', 'house': ''}

        new_dict['first'] = dict['name'][1]
        new_dict['last'] = dict['name'][0]
        new_dict['house'] = dict['house']
        new_list.append(new_dict)

    return new_list

#write_file finally creates a new csv file that takes a dict a writes each row in the csv file.
def write_file(dict):

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for item in dict:
            writer.writerow({"first": item['first'], 'last': item['last'], 'house': item['house'] })


if __name__ == "__main__":
    main()
