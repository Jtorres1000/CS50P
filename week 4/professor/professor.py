import random
#Main loop, creates a value variable of 0, that stores the level.
def main():

    check_answers(generate_integer(get_level()))

#Get_level function simply ask for a input of a level to the user if any of the wrong conditions is made it would rise type error o valueError.
def get_level():
    while True:
        try:
            level = int(input("Level:"))
            if level < 0 or level == 0 or level > 3:
                raise TypeError
        except ValueError:
            pass
        except TypeError:
            pass
        else:
            return level

#i made Generate_integer a little different from what they ask in the page, it creates a dict and stores random int values as follows: [Correct Answer, The Exersice, The result as intenger] then it returns that dict
def generate_integer(n):
    if n == 1:
        max = 9
        min = 0

    elif n == 2:
        max = 99
        min = 10

    else:
        max = 999
        min = 100
        
    exercise_list = {}

    for i in range(0, 10):
        x = random.randint(min, max)
        y = random.randint(min, max)
        c = x + y
        exercise_list[i] = [f"{x} + {y} = {c}", f"{x} + {y} = ", c]

    return exercise_list

#Check answers has a parameter that has to be the dict and it goes through it to get all the exercises and ask the user for the answers, based on whether it is incorrect or correct it saves the results in a dict and finally prints the score.
#It also takes care that typing errors make the attempt lost.

def check_answers(dict):
    results = {"wrong": 0, "correct" : 0}

    for exercise in dict:
        attemps = 0

        while True:
            try:
                attemps += 1
                answer = int(input(dict[exercise][1]))
                if answer == dict[exercise][2]:
                    results["correct"] += 1
                    break
                elif attemps == 3:
                    print("EEE")
                    print(dict[exercise][0])
                    results["wrong"] += 1
                    break
                else:
                    print("EEE")
                    if attemps  < 3:
                        continue
            except ValueError:
                if attemps == 3:
                    print("EEE")
                    print(dict[exercise][0])
                    results["wrong"] += 1
                    break
                else:
                    print("EEE")

    score = results["correct"]

    print(f"score: {score}")


if __name__ == "__main__":
    main()
