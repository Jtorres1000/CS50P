from validator_collection import validators

def main():
    print(check(input("What's your email address? ")))

#uses validators.email module to validate the user input
def check(s):
    try:
        validators.email(s)
    except ValueError:
        return "Invalid"

    else: return "Valid"

if __name__ == "__main__":
    main()
