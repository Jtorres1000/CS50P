#We define a main fuction that contains the main part of the program.
def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# We define is_valid that returns True only if al conditions are meet.

def is_valid(s):
    if word_size(s) and all_numbers(s) and s.isalnum() and ends_with(s):
        return True
    else: return False

#Word_size returns true if the word length is between 2 an 6
def word_size(str):
    return 2 <= len(str) <= 6

#All_numbers checks if the word is all digits, otherwise it returns true
def all_numbers(str):
    if str.isdigit():
        return False
    else: return True

#ends_with veriefies that theres not numbers in the middle, and checks that the first number is not zero.
def ends_with(string):

    if string.isalpha():
        return True

    for i, char in enumerate(string):
        if char.isdigit():
            if string[i] == "0":
                return False
            for next_char in string[i + 1:]:
                if not next_char.isdigit():
                    return False
            return True
    return False

#we call the main function
main()

