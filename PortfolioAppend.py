from PyPDF3 import PdfFileMerger
import os
from datetime import date
from os import listdir


def main():
    folder_name = str(date.today())
    folder_location = os.path.join(
        r'/Users/briandunn/Documents/Job_Search_2021/', folder_name)

    #print("File path to the docx files folder: ", folder_location)
    os.chdir(folder_location)
    #current_location = os.getcwd()
    #print("Current Location: ", current_location)

    portfolio_to_merge = r'/Users/briandunn/Documents/Job_Search_2021/Brian Dunn-Portfolio.pdf'
    #print("Portfolio: ", portfolio_to_merge)

    # select all of the PDF files only
    pdf_only = r'.pdf'
    list_of_resumes = [x for x in listdir(os.getcwd()) if x.endswith(pdf_only)]

    # Append the portfolio to the end of the resume
    for i in range(len(list_of_resumes)):
        portfolio_appender = PdfFileMerger()
        resumeInput = open(list_of_resumes[i], 'rb')
        PortfolioInput = open(portfolio_to_merge, 'rb')
        portfolio_appender.append(resumeInput)
        portfolio_appender.append(PortfolioInput)
        output = open(list_of_resumes[i], 'wb')
        portfolio_appender.write(output)


if __name__ == '__main__':
    main()
    quit()
