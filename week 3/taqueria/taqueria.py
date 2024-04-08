#We define a main fuction that contains the main part of the program.

def main():
    #We call the total_list function.

    total_list()

    #Total_list function is a while loop that ask for input and sums the value found by search_item function to total.
    #if we press control+d it'll stop the loop otherwise it'll continue.

def total_list():
    total = 0
    while True:
        try:
            item = input("Item:\n")
            total += search_item(item)

        except EOFError:
            break

        except KeyError:
            pass

        else:
            formatted_total = f"${total:.2f}"
            print(formatted_total)

    #search_item simply returns the item, if it not found the key it will return a KeyError:
def search_item(item):

    items = {
            "Baja Taco": 4.25,
            "Burrito": 7.50,
            "Bowl": 8.50,
            "Nachos": 11.00,
            "Quesadilla": 8.50,
            "Super Burrito": 8.50,
            "Super Quesadilla": 9.50,
            "Taco": 3.00,
            "Tortilla Salad": 8.00
        }

    return items[item.title()]

    #Calling the main function
main()


