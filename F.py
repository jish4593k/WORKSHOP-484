import fitz  

def parse(pdf_filename):
    
    pdf_document = fitz.open(pdf_filename)

    # Create a text file to store the extracted text
    with open('output.txt', 'w', encoding='utf-8') as output_file:
       
        for page_num in range(pdf_document.page_count):
            # Get the page
            page = pdf_document[page_num]

            # Get the text from the page
            text = page.get_text()

            # Print the text to the console
            print(text)

            output_file.write(text + '\n')

if __name__ == '__main__':
   
