import fitz
import time


pdf_path = 'Australia National Inventory.pdf'
output_txt = 'output_pymupdf.txt'

start_time = time.time()
doc = fitz.open(pdf_path)


with open(output_txt, 'w', encoding='utf-8') as f:
    for page in doc:
        text = page.get_text("text")
        f.write(text)
end_time = time.time()


process_time = end_time - start_time

print(f"Text extracted and saved to {output_txt}")
print(f"Process time: {process_time:.2f} seconds")