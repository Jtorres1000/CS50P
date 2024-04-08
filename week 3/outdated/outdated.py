#We define a main fuction that contains the main part of the program.

def main():
    #we call take_input fuction.
    take_input()

    #take input function its a while loop that calls 1 of 2 fuctions checking if it has MM/DD/YYYY format or latter format, and prints the result.
def take_input():

    while True:
        try:
            value = input('Date: \n').strip()

            if "/" in value:
                date = split_one(value)

            elif "," in value:
                date = split_two(value)

            else:
                raise TypeError

        except TypeError:
            pass
        else:
            print(date)
            break

#Split_one function handles MM/DD/YYYY format and returns the YYYY/MM/DD format.

def split_one(string):

    string = string.split("/")

    for value in string:
        if not value.isnumeric():
            raise TypeError

    if int(string[0]) > 12 or int(string[1]) > 31:
        raise TypeError

    if int(string[0]) < 10:
        string[0] = str(string[0]).zfill(2)

    if int(string[1]) < 10:
        string[1] = str(string[1]).zfill(2)

    date = f"{string[2]}-{string[0]}-{string[1]}"

    return date

#Split_two function handles the latter format and returns it in YYYY/MM/DD format

def split_two(string):

    months_dict = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
    }

    string = string.replace(",", "")
    string = string.split(" ")
    string[0] = string[0].capitalize()

    try:
        if int(string[1]) > 31:
            raise TypeError
    except ValueError:
        pass

    if string[0] in months_dict:

        string[0] = months_dict[string[0]]

        if string[0] < 10:
            string[0] = str(string[0]).zfill(2)

        if int(string[1]) < 10:
            string[1] = str(string[1]).zfill(2)

        date = f"{string[2]}-{string[0]}-{string[1]}"

        return date

    else:
        raise TypeError

main()
