from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter

reader = PdfReader("C:\\Users\\vatsa\\Downloads\\220280116044_CompletionCertificate.pdf")

page = reader.pages[0]

print(page.extract_text())

# writer = PdfWriter()

# writer.add_page(page)

# writer.write("C:\\Users\\vatsa\\Downloads\\220280116044_CompletionCertificate.docx")
# writer.close()
# print("Done")

