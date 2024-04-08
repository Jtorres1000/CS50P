#We define a main fuction that contains the main part of the program.

def main():
    #We take user input with input function and store it.
    greeting = input("Enter the file name:\n")

    #We call extension function.
    extension(greeting)

    #We define extension that has a dictionary with each indivual key extension and a value, them with use a for loop to iterate through all keys and check if any of them is equal to the extension of the user input if its true, it enable the extension_found and prints the value of the key, otherwise it prints application/octet-stream.
def extension(input):
    #Note: i don't know if my approach to this problem it's ok because this topic hasn't be cover in the course yet, so i apologyze is thats the case.

    list_of_extensions = {
        ".gif" : "image/gif",
        ".jpg" : "image/jpeg",
        ".jpeg" : "image/jpeg",
        ".png" : "image/png",
        ".pdf" : "application/pdf",
        ".txt" : "text/plain",
        ".zip" : "application/zip"
        }

    extension_found = False

    input = input.strip().casefold()

    for extension in list_of_extensions:
        if input.endswith(extension):
            extension_found = True
            print(f"{list_of_extensions[extension]}")

    if extension_found == False:
        print("application/octet-stream")

    #Calling the main function
main()
