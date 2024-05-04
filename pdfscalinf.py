from PyPDF2 import PdfReader, PdfWriter

# Read the input
reader = PdfReader("C:\\Users\\vatsa\\Downloads\\M.pdf")
page = reader.pages[0]

# Scale
page.scale_by(1)

from PyPDF2.generic import RectangleObject

mb = page.mediabox

page.mediabox = RectangleObject((mb.left, mb.bottom, mb.right, mb.top))
page.cropbox = RectangleObject((mb.left, mb.bottom, mb.right, mb.top))
page.trimbox = RectangleObject((mb.left, mb.bottom, mb.right, mb.top))
page.bleedbox = RectangleObject((mb.left, mb.bottom, mb.right, mb.top))
page.artbox = RectangleObject((mb.left, mb.bottom, mb.right, mb.top))
# Write the result to a file
writer = PdfWriter()
writer.add_page(page)
writer.write("out.pdf")