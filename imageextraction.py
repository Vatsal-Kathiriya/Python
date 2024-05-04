from PyPDF2 import PdfReader
from PyPDF2 import PdfWriter



reader = PdfReader("C:\\Users\\vatsa\\Downloads\\GSRTC.pdf")

page = reader.pages[0]

count = 0
for image_file_object in page.images:
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data) 
    count += 1

    # print(page.extract_text())
    print(image_file_object.name)
    # print(image_file_object.data)
    