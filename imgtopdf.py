# import fitz

# # open document 

# doc = fitz.open() 
# imgdoc = fitz.open("E:\\Downloads\\_9fc614c7-cffb-49a1-b510-93810f9741ae.jpeg") # open image 
# pdfbytes = imgdoc.convert_to_pdf() 
# imgpdf = fitz.open("pdf", pdfbytes) 
# doc.insert_pdf(imgpdf) 
# doc.save('imagetopdf.pdf') # save file 

# Python3 program to convert image to pdf
# using img2pdf library

# importing necessary libraries
import img2pdf
from PIL import Image
import os

# storing image path
img_path = "C:\\Users\\vatsa\\Downloads\\Merged_document.jpg"

# storing pdf path
pdf_path = "file1.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")
