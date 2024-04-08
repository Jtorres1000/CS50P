import re

#Main function takes the user input.
def main():
    print(validate(input("IPv4 Address: ").strip()))
#validate function takes the input a search for a match that follows this pattern "num.num.num.num" and catches the groups, then it sees if any of the groups are bigger than 255 if that not the case it returns True
def validate(ip):

    matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
    if matches:
        for i in range(1,5):
            print(matches.group(i))
            x = int(matches.group(i))

            if x > 255 or x < 0:
                return False

        return True

    else: return False

if __name__ == "__main__":
    main()
