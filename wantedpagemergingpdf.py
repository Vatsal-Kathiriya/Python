from PyPDF2 import PdfWriter

merger = PdfWriter()

input1 = open("C:\\Users\\vatsa\\Downloads\\Hands-on-Machine-Learning (1).pdf", "rb")
input2 = open("C:\\Users\\vatsa\\Downloads\\Hands-On Machine Learning with Scikit-Learn and TensorFlow_ Concepts, Tools, and Techniques to Build Intelligent Systems - PDF Room.pdf", "rb")
input3 = open("C:\\Users\\vatsa\\Downloads\\Hands-on-Machine-Learning.pdf", "rb")
# input4 = open("C:\\Users\\vatsa\\Downloads\\GSRTC.pdf", "rb")

# add the first 3 pages of input1 document to output
merger.append(fileobj=input1, pages=(0, 5))

# insert the first page of input2 into the output beginning after the second page
merger.merge(position=5, fileobj=input2, pages=(0,1))
# insert the first page of input3 into the output beginning after the second page
# merger.append(fileobj=input2, pages=(0, 5)) 

# merger.merge(position=3, fileobj=input4, pages=(0, 1))

# append entire input3 document to the end of the output document
merger.append(fileobj=input3 , pages=(0,5))

# Write to an output PDF document
output = open("document-output.pdf", "wb")
merger.write(output)

# Close File Descriptors
merger.close()
output.close()