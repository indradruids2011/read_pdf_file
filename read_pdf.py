import PyPDF2
import tabula
import camelot

###################################################
# PyPDF2
###################################################
pdfFileObj = open('downloads.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
###################################################


###################################################
# tabula
###################################################
file = "downloads.pdf"
table = tabula.read_pdf(file, pages=1, stream=True)
table[0]
###################################################


###################################################
# camelot
###################################################
# PDF file to extract tables from
file = "downloads.pdf"
tables = camelot.read_pdf(file, strip_text=' .\n')
# number of tables extracted
print("Total tables extracted:", tables.n)
# export individually
tables[1].to_csv("test2.csv")
###################################################
