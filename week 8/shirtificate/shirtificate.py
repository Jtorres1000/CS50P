from fpdf import FPDF

def main():
    name = input("Name: ")
    create_pdf(name)

def create_pdf(name):
    #creates a FPDF object
    pdf = FPDF()
    #adds a new page
    pdf.add_page()
    #sets the font style
    pdf.set_font("Times", size=32, style="B")
    #creates a text cell that is centered horizontally and is at the top of the page.
    pdf.cell(text="CS50 Shirtificate", align="C", center=True)
    #imports the shirt png resizes it and put its in y 40 position
    pdf.image("./shirtificate.png", x= "C", y=40, w= 180)
    #change the font size
    pdf.set_font("Times", size=18, style="B")
    #change font color to white
    pdf.set_text_color(255)
    #making blank spaces
    pdf.ln(90)
    #putting the username on the shirt.
    pdf.cell(text=f"{name} took CS50", align="C", center=True)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
