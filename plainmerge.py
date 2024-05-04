from PyPDF2 import PdfReader, PdfWriter, Transformation

# Get the data
reader_base = PdfReader("C:\\Users\\vatsa\\Downloads\\M.pdf")
page_base = reader_base.pages[0]

reader = PdfReader("E:\\Downloads\\ACK439733310120723.pdf")
page_box = reader.pages[0]

page_base.merge_page(page_box)

# Write the result back
writer = PdfWriter()
writer.add_page(page_base)
with open("merged-foo.pdf", "wb") as fp:
    writer.write(fp)