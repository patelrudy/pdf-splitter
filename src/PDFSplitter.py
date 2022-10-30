import PyPDF2 as pdf


def pdf_splitter(file, newFileName, startPage, endPage):

    read_pdf = readPDF(file)
    newFileName += ".pdf"
    flag = 1

    while flag:
        if (endPage < read_pdf.getNumPages() and startPage < endPage):
            flag = 0
        else:
            print("Please check you pdf")
            status = int(input(
                "press 0 to change the startpage, press 1 to change the endpage, press 2 to change the pdf: "))
            if status == 0:
                startPage = int(input("enter updated startpage: ")) - 1
            if status == 1:
                endPage = int(input("enter updated endpage: "))
            if status == 2:
                file = input("orginal pdf path/name: ")
            read_pdf = readPDF(file)

    try:
        split_pdf = pdf.PdfFileWriter()
        for pageNumber in range(startPage, endPage):
            split_pdf.addPage(read_pdf.getPage(pageNumber))

        with open(newFileName, "wb") as file:
            split_pdf.write(file)
    except:
        print("Error Occurred: Please re-enter all parameters")
        getInput()


def getInput():
    file = input("Please enter file path with extension: ")
    newFileName = input("please enter split pdf name without extension: ")
    startPage = int(input("please enter start page to split from: ")) - 1
    endPage = int(input("Please enter the end page to stop the split at: "))
    pdf_splitter(file, newFileName, startPage, endPage)


def readPDF(filename):
    read_pdf = pdf.PdfFileReader(filename)
    return read_pdf


getInput()
