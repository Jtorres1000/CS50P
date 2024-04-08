#We define a main fuction that contains the main part of the program.
def main():
    #We call coke_dispenser function.
    coke_dispenser()

    #defining the coke_dispenser function.
def coke_dispenser():
    #we set the amount_due to 50
    amount_due = 50

    while True:
        #we check if there is a amount_due otherwise it means there's no more due, and prints the amounts and breaks the while loop.
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
            coin = int(input("Insert Coin: "))
        else:
            print(f"Change Owed: {amount_due * -1}")
            break

        #We check with its_valid function to see if the coin it's a valid coin otherwise it wont change amount_due
        if its_valid(coin):
            amount_due -= coin

def its_valid(amount):
    return amount in [25, 10, 5]


    #calling main function.
main()
