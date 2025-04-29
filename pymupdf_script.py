import fitz  # PyMuPDF

# PDF path and output text file
pdf_path = 'DRAFT_NID_2024_Albania_20241231.pdf'
output_txt = 'output_pymupdf.txt'

# Open the PDF
doc = fitz.open(pdf_path)

# Extract text and write to a text file
with open(output_txt, 'w', encoding='utf-8') as f:
    for page in doc:
        # Extract text from each page
        text = page.get_text("text")  # You can also use "blocks" or "dict" for more complex layout
        f.write(text)

print(f"Text extracted and saved to {output_txt}")
