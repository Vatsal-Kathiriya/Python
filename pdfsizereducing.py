from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("C:\\Users\\vatsa\\Downloads\\M.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.add_metadata(reader.metadata)

with open("smaller-new-file.pdf", "wb") as fp:
    writer.write(fp)