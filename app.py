from fortunes import fortune_gen
from fpdf import FPDF
# https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
# fpdf https://py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF

# ask for name
# ask for birthday
# take random number from birthday / 365 then use that to pick a fortune or pick randomly
class PDF():
    def __init__(self, name_input, fortune):
        self._pdf = FPDF()
        self._pdf.set_page_background(background="lulu.jpg")
        self._pdf.add_page()
        self._pdf.set_auto_page_break(auto=False, margin=0)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font("Helvetica", "B", 30)
        self._pdf.cell(0, 50, "lulu says your fortune is:", new_x="LMARGIN", new_y="NEXT", align="C")

        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font("Helvetica", "B", size=30)
        self._pdf.cell(w=0, h=250, text=f"{name_input}, ", new_x="LMARGIN", align="L")

        self._pdf.set_text_color(255, 255, 255)
        self._pdf.set_font("Helvetica", "B", size=15)
        self._pdf.cell(w=0, h=270, text=f"{fortune}", new_x="LMARGIN", new_y="NEXT", align="L")

    def save(self, name_input):
        self._pdf.output(name_input)

def main():
    name_input = input("Whats your name? ")
    fortune = fortune_gen()
    pdf = PDF(name_input, fortune)
    pdf.save("fortune.pdf")




if __name__ == "__main__":
    main()
