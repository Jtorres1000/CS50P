def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# First we filter the $ symbols then we convert it to float and return it.
def dollars_to_float(d):
    d = float(d.replace("$", ""))
    return d

#First we filter the % symbols, then we convert it to float, divide it by 100 and return it.
def percent_to_float(p):
    p = float(p.replace("%", "")) / 100
    return p

main()
