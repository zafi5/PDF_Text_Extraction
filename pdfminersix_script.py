import os
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import logging
logging.getLogger("pdfminer").setLevel(logging.ERROR)

# Set layout analysis parameters
laparams = LAParams(
    line_overlap=0.5,
    char_margin=2.0,
    line_margin=0.5,
    word_margin=0.1,
    boxes_flow=0.5
)

# Extract text from the PDF
pdf_path = 'DRAFT_NID_2024_Albania_20241231.pdf'
output_txt = 'output_pdfminersix.txt'
text = extract_text(pdf_path, laparams=laparams)

# Write the text to a .txt file
with open(output_txt, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Text extracted and saved to {output_txt}")
