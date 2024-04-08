import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    #search for a pattern of (1 or 2 digits):(1 ir 2 digits or not) (am or pm) to  (1 or 2 digits):(1 ir 2 digits or not) (am or pm again)
    if matches := re.search(r"^(\d{1,2})(?::(\d{1,2}))? (am|pm) to (\d{1,2})(?::(\d{1,2}))? (?:pm|am)", s, re.IGNORECASE):

        #Assigns the values of match groups in variables
        hours_one = int(matches.group(1))
        minutes_one = int(matches.group(2)) if matches.group(2) else 0
        time= matches.group(3)
        hours_two = int(matches.group(4))
        minutes_two = int(matches.group(5)) if matches.group(5) else 0

        #check if the hours and minutes are correct values
        if hours_one > 12 or hours_two > 12 or minutes_one > 59 or minutes_two > 59:
            raise ValueError
        #if time is am adds 12 to the secound hour only if  hours one is not 12, in which case it subtracts 12 from the first hours.
        if time == "am" or time == "AM":
            if hours_one == 12:
                return f"{str(hours_one - 12).zfill(2)}:{str(minutes_one).zfill(2)} to {str(hours_two).zfill(2)}:{str(minutes_two).zfill(2)}"
            else: return f"{str(hours_one).zfill(2)}:{str(minutes_one).zfill(2)} to {str(hours_two + 12).zfill(2)}:{str(minutes_two).zfill(2)}"

        #if time is pm does the same thing but inverting it add 12 to the first hours, or subtracts 12 from the second hours.
        else:
            if hours_two == 12:
                return f"{str(hours_one).zfill(2)}:{str(minutes_one).zfill(2)} to {str(hours_two - 12).zfill(2)}:{str(minutes_two).zfill(2)}"
            else: return f"{str(hours_one + 12).zfill(2)}:{str(minutes_one).zfill(2)} to {str(hours_two).zfill(2)}:{str(minutes_two).zfill(2)}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
