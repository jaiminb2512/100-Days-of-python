# Write a program to manipulate pdf files using pyPDF. Your programs should be able to merge multiple pdf files into a single pdf. You are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping, and transforming the pages of PDF files. It can also add custom data, viewing options, and passwords to PDF files. pypdf can retrieve text and metadata from PDFs as well.

import os
import PyPDF2

# Function to get a list of PDF files in a folder
def get_pdf_files_in_folder(folder_path):
    pdf_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

# Function to merge PDFs from a list of file paths
def merge_pdfs(pdf_files, output_file):
    pdf_merger = PyPDF2.PdfFileMerger()
    for pdf_file in pdf_files:
        pdf_merger.append(pdf_file)
    pdf_merger.write(output_file)
    pdf_merger.close()

# Specify the folder containing your PDF files
folder_path = "path_to_your_folder"  # Replace with your folder path

# Get a list of PDF files in the folder
pdf_files_list = get_pdf_files_in_folder(folder_path)

# Specify the output file name
output_file = "merged.pdf"  # You can change the output file name if needed

# Merge the PDFs
merge_pdfs(pdf_files_list, output_file)

print(f"{len(pdf_files_list)} PDFs merged into {output_file}")
