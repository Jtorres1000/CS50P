#Import inflect module
import inflect
#Store the inflect engine in a global variable
p = inflect.engine()

def main ():
    #A while loop that keep asking for inputs until the user press contro + D AKA EOFError.
    list_names = []
    while True:
        try:
            add_name(list_names)
        except EOFError:
            adieu_names(list_names)
            break

#Just ask for a name and add the name to the list.
def add_name(list):

    name = input("Name: ")
    list.append(name)

#Join the list using the inflect module join method and prints it.
def adieu_names(list):

    ready_names = p.join(list)
    print(f"Adieu, adieu, to {ready_names}")

main()
