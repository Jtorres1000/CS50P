#We define a main fuction that contains the main part of the program.

def main():
    #We take user input with input function convert it to integer and store it.
    mass = int(input("Enter the mass to convert (in kilograms): \n"))

    #We call the mass_convert function.
    mass_convert(mass)

    #we define mass_convert it uses the E = mc^2 formula to get the joules equivalent of the mass and print it.
def mass_convert(mass):
    speed_of_light = 300000000
    joules = mass * speed_of_light ** 2

    print(joules)

    #Calling the main function
main()


