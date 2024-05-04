from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("C:\\Users\\vatsa\\Downloads\\M.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.remove_images()

with open("out.pdf", "wb") as f:
    writer.write(f)