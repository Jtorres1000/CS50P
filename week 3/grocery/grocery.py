#We define a main fuction that contains the main part of the program.

def main():
    #We declare a empty dic in the main scope to keep track of the list of grocery's.

    dic = {}

    while True:
        try:
            add_list(dic)

        except EOFError:
            print_list(sort_dic(dic))
            break

#Add_list function takes a dic a ask for a value to add it to the dictionary, if is already it's there it just adds one to the value of the key.
def add_list(dic):

    value = input()
    if value in dic:
        dic[value] += 1
    else:
        dic[f'{value.lower()}'] = 1

#sort_dic function takes a dic and returns a new one sorted based on key values. it first takes the dic and converts it into a tuple, then uses the sorted method to sort the tuples by their "key", and finally uses a comprehension dictionary to make a new one based on the tuples.
def sort_dic(dic):

    sort_dic = {k: v for k, v in sorted(dic.items())}
    return sort_dic

#print_list function use a for loop to loop through the dic and prints the value of the key and the key itself.
def print_list(dic):

    for grocery in dic:
        print(f"{dic[grocery]} {grocery.upper()}")

    #Calling the main function
main()


