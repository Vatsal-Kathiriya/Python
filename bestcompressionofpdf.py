# from PyPDF2 import PdfReader, PdfWriter

# reader = PdfReader("C:\\Users\\vatsa\\Downloads\\M.pdf")
# writer = PdfWriter()

# for page in reader.pages:
#     page.compress_content_streams()  # This is CPU intensive!
#     writer.add_page(page)

# with open("out.pdf", "wb") as f:
#     writer.write(f)


# from ironpdf import *


# # Apply your license key

# License.LicenseKey = "IRONSUITE.TELAW89538.HAISLOT.COM.5563-4922AA463E-BDXD3EBLGNXBBMCB-NLRBUHNC6LTK-NFGOGZVQMXAI-C6RIKMDXDSL4-7LN3BKVYUOU2-Z7CBZJAW6YP2-Y7E6PT-T4JKN4DA3EOMUA-DEPLOYMENT.TRIAL-5OCU5K.TRIAL.EXPIRES.27.MAY.2024";


# pdf = PdfDocument("C:\\Users\\vatsa\\Downloads\\M.pdf")

# # Quality parameter can be 1-100, where 100 is 100% of original quality
# pdf.CompressImages(1)
# pdf.SaveAs("document_compressed.pdf")

# # Second optional parameter can scale down the image resolution according to its visible size in the PDF document. Note that this may cause distortion with some image configurations
# pdf.CompressImages(90, True)
# pdf.SaveAs("Compressed.pdf")
