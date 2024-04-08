import sys
#Main function, prints out the outpout of the functions and handle errors in user input.
def main ():

    try:
        handle_arg()
        print(count_lines(open_read()))

    except TypeError:
        sys.exit("Too few command-line arguments")
    except ValueError:
        sys.exit("Too many command-line arguments")
    except NameError:
        sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")

#Handle_arg, makes sure that there's not error with the user input.
def handle_arg():

    if len(sys.argv) == 1:
        raise TypeError
    if len(sys.argv) > 2:
        raise ValueError

    elif not sys.argv[1].endswith(".py"):
        raise NameError
#Open_read opens the file an then get a list with readlines an strip them with a foor loop.
def open_read():

    file = open(sys.argv[1], "r")

    file_list = file.readlines()

    file.close()

    for i in range(len(file_list)):
        file_list[i] = file_list[i].strip()

    return file_list

#count_lines takes a list and then finds and counts any line that is not an empty line or a comment.
def count_lines(list):
    count = 0

    for line in list:
        if line == "":
            pass
        elif line.startswith("#"):
            pass
        else:
            count += 1

    return count


if __name__ == "__main__":
    main()
