from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():
    pdf.add_page()

    # Set the Header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="L")

    # Draw a horizontal line
    y1, y2 = 21, 21
    for i in range(0, 265, 10):
        pdf.line(10, y1, 200, y2)
        y1 += 10
        y2 += 10

    # Set the footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="R")

    for i in range(row["Pages"]-1):
        pdf.add_page()

        # Draw a horizontal line
        y1, y2 = 21, 21
        for i in range(0, 265, 10):
            pdf.line(10, y1, 200, y2)
            y1 += 10
            y2 += 10

        # Set the footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="R")

pdf.output("output.pdf")
