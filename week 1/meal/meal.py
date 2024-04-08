def main():
    #We take user input with input function and store it.
    #Note i made the challenge part it was a difficult task i know that my code it's a mess, but i can't see in other way of get it hahaha.
    time = input("what time is it?\n")

    #I handle 3 cases, 1 when the time given it's not in 12-hour times, other when time given it's 12-hour times and it's morning time, and a last one when it's 12-hour times but night time.
    if time.endswith("p.m."):
        convert(time, True, True)
    elif time.endswith("a.m."):
        convert(time, True)
    else:convert(time)

def convert(time, twelve = False, night = False):
    #if the value it's 12-hour times it'll first elimate the p.m. or a.m. from the string in order to convert it on intenger.
    if twelve == True:
        time = time[:-4]
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

    #Them if the hours are not equal to 12 and it's night it will add 12 to the hours in order to get the correct conversion to food_time handle the integer value properly

        if hours != 12 and night == True:
            hours +=12
        food_time(((hours * 60) + minutes) / 60)
        return (((hours * 60) + minutes) / 60)
    else:
    #otherwise it'll do the calculations normally because the morning hours in 24-hour times and 12-hour times are equal.
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)
        food_time(((hours * 60) + minutes) / 60)
        return (((hours * 60) + minutes) / 60)

    #finally, food_time handles the intenger value given by convert to determinate whitch  meal time is.
def food_time(what_time):

    if what_time >= 7 and what_time <= 8:
        print("breakfast time")
    elif what_time >= 12 and what_time <= 13:
        print("lunch time")
    elif what_time >= 18 and what_time <= 19:
        print("dinner time")
    else: return 0

    #I hope my comments helps to understand the logic in my code it was fun to solve the challenge!
if __name__ == "__main__":
    main()

