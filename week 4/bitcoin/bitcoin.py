#Importing requests and sys modules
import requests
import sys
#Using main loop to get the command line argument, and check if is correct.

def main():
    try:
        n = sys.argv[1]
        if n.isalpha():
            raise TypeError
        else:
            check_bit(n)

    except ValueError:
        sys.exit("Not a valid float")
    except TypeError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line argument")

#Makes a request to the API of coindesk to get the current price and the it multiplies it with the command line input.

def check_bit(n):
    n = float(n)
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    except requests.RequestException:
        print("Error request!")
    else:
        response_j = response.json()
        rate = response_j["bpi"]["USD"]["rate_float"]
        user_total = rate * n
        print(f"${user_total:,.4f}")

main()
