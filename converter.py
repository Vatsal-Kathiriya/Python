# from pdf2docx import parse

# p = r"C:\\Users\\vatsa\\Downloads\\220280116044_CompletionCertificate.pdf"

# d = r"C:\\Users\\vatsa\\Downloads\\220280116044_CompletionCertificate.docx"

# parse(p, d)

# print("PDF to DOCX conversion complete.")

from pdf2docx import Converter

p = r"C:\\Users\\vatsa\\Downloads\\220280116044_CompletionCertificate.pdf"

d = r"C:\\Users\\vatsa\\Downloads\\220280116044_CompletionCertificate.docx"

cv = Converter(p)

cv.convert(d)

cv.close()

print("PDF to DOCX conversion complete.")