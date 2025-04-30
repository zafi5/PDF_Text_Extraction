import os
from pdfminer.high_level import extract_text
from pdfminer.layout import LAParams
import logging
import time


logging.getLogger("pdfminer").setLevel(logging.ERROR)


laparams = LAParams(
    line_overlap=0.5,
    char_margin=2.0,
    line_margin=0.5,
    word_margin=0.1,
    boxes_flow=0.5
)


pdf_path = 'Australia National Inventory.pdf'
output_txt = 'output_pdfminersix.txt'


start_time = time.time()


text = extract_text(pdf_path, laparams=laparams)


with open(output_txt, 'w', encoding='utf-8') as f:
    f.write(text)


end_time = time.time()
process_time = end_time - start_time


print(f"Text extracted and saved to {output_txt}")
print(f"Process time: {process_time:.2f} seconds")
