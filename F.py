import fitz  # PyMuPDF

def parse(pdf_filename):
    # Open the PDF file
    pdf_document = fitz.open(pdf_filename)

    # Create a text file to store the extracted text
    with open('output.txt', 'w', encoding='utf-8') as output_file:
        # Iterate through each page in the PDF
        for page_num in range(pdf_document.page_count):
            # Get the page
            page = pdf_document[page_num]

            # Get the text from the page
            text = page.get_text()

            # Print the text to the console
            print(text)

            # Write the text to the output file
            output_file.write(text + '\n')

if __name__ == '__main__':
    parse('重新发现官僚制西方公共行政理论对官僚制的再思考.pdf')
