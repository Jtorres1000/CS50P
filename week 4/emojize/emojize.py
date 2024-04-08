#We import emoji module to use it
import emoji

#We ask the user for and input.
def main():

    emoji = input("Input\n")
    extension(emoji)

#We use the function emojize() along with the argument language="alias" to admit alias in the input.
def extension(string):

    print(f"{emoji.emojize(string, language='alias')}")

main()
