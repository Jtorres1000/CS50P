#We define a main fuction that contains the main part of the program.
def main():

    #We take user input with input function and store it.
    user_input = input("Item:\n")

    #we make sure that the input has no capital letters.
    user_input = user_input.casefold()

    #We call calories function.
    calories(user_input)

    #defining the calories function.
def calories(input):
    #We define a dictionary with the fruits name as key and the fruits calories as value.

    fruit_list = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew melon': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80
}
    #them we simply iterate in the fruit list to see if any of the fruits it's equal to the user input and prints out the calories value, otherwise it returns a empty string.
    for fruit in fruit_list:
        if fruit == input:
            print(f"Calories:{fruit_list[fruit]}")
    return ""

main()
