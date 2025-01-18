from fpdf import FPDF

def Convert_And_Download_Subtitle(text):
    # create a pdf object
    pdf = FPDF()
    # add a page to the pdf
    pdf.add_page()
    # set font and size of the font
    pdf.set_font("Arial", size=12)
    # for evey line in the text
    for line in text.split('\n'):
        # add the line to the pdf
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    
    # save and download the pdf with a custom file name
    pdf.output("subtitle.pdf")