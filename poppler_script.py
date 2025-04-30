import subprocess
import time


pdf_path = 'Australia National Inventory.pdf'
output_txt = 'output_poppler.txt'


start_time = time.time()


command = ['pdftotext', pdf_path, output_txt]
subprocess.run(command, check=True)


end_time = time.time()


process_time = end_time - start_time
print(f"Text extracted and saved to {output_txt}")
print(f"Process time: {process_time:.2f} seconds")
