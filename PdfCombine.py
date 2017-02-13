#! python3
# PdfCombine.py - Combine all the PDFs in the current working directory into one

import PyPDF2, os

# Get all the PDF filenames
pdfFiles = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)

pdfFiles.sort(key=str.lower)    # sorting the file in alphabetic order

pdfWriter = PyPDF2.PdfFileWriter()

# Loop through all the PDF files
for filename in pdfFiles:
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # Loop through all pages
    for pageNum in range(pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

# Save the resulting PDF to a file
pdfOutput = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()