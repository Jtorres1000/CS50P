import sys
from PIL import Image, ImageOps

#Main function, handle errors in user input and calls the function that creates the new file.
def main ():

    try:
        handle_arg()
        create_img()

    except TypeError:
        sys.exit("Too few command-line arguments")
    except ValueError:
        sys.exit("Too many command-line arguments")
    except NameError:
        sys.exit("Invalid output")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    except KeyError:
        sys.exit("Input and output have different extensions")

#Handle_arg, makes sure that there's not error with the user input.
def handle_arg():
    extensions = []

    if len(sys.argv) < 3:
        raise TypeError
    if len(sys.argv) > 3:
        raise ValueError

    for item in sys.argv[1:]:
        extensions.append(item.split("."))

    if extensions[1][1] not in ["jpg","jpeg","png"]:
        raise NameError

    if extensions[0][1] != extensions[1][1]:
        raise KeyError
    
#create_img first open the shirt.png image and the first input image, then crop the first image, and superimpose the shirt.png photo over the first one and finally save that new_image in sys.argv[2]
def create_img():
    shirt = Image.open("shirt.png")
    image = Image.open(sys.argv[1])
    new_image = ImageOps.fit(image, (600, 600))
    new_image.paste(shirt, shirt)
    new_image.save(sys.argv[2])

if __name__ == "__main__":
    main()
