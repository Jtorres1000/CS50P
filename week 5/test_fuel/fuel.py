def main():

        while True:
            try:
                value = input("Fraction:\n")
                print(gauge(convert(value)))
            except ValueError:
                pass
            except ZeroDivisionError:
                pass
            else:
                break

def convert(fraction):

    str_list = fraction.split("/")

    lst = list(map(lambda x: int(x), str_list))

    if lst[1] == 0:
        raise ZeroDivisionError
    
    if lst[0] > lst[1]:
        raise ValueError



    division = round((lst[0] / lst[1]) * 100)

    return division

def gauge(percentage):

    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
