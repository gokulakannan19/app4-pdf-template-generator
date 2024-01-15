from fpdf import FPDF
import pandas as pd

df = pd.read_csv("topics.csv")
pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], border=0, ln=1, align="L")
    pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")
