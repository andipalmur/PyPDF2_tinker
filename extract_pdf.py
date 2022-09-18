# importing required modules
import PyPDF2

# creating a pdf file object
pdf_file_obj = open('/home/andy/Documents/brendastone_project_folders/pdfs/ancient_egypt_dictionary.pdf', 'rb')
	
# creating a pdf reader object
reader = PyPDF2.PdfReader(pdf_file_obj)
	
# printing number of pages in pdf file
print(len(reader.pages))

for p in range(0,20):
    # creating a page object
    page_obj = reader.pages[p]
        
    # extracting text from page
    print(page_obj.extract_text())
	
# closing the pdf file object
pdf_file_obj.close()