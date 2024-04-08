def main():

    user_input = input("Input:\n")


    print(shorten(user_input))

def shorten(word):

    table = str.maketrans("", "", "aeiouAEIOU")

    return word.translate(table)

if __name__ == "__main__":

    main()
