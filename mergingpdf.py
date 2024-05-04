from PyPDF2 import PdfWriter

merger = PdfWriter()

for pdf in ["E:\\Downloads\\1.pdf", "E:\\Downloads\\2.pdf", "E:\\Downloads\\3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")

merger.close()