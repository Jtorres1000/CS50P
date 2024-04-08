def main():

    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if word_size(s) and all_numbers(s) and s.isalnum() and ends_with(s):
        return True
    else: return False


def word_size(str):
    return 2 <= len(str) <= 6


def all_numbers(str):
    if str.isdigit():
        return False
    else: return True


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

if __name__ == "__main__":
    main()
