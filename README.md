# Automation-with-Python

This Python script automates the process of renaming PDF files based on an Excel file. The Excel file contains two columns: one for the old file names and one for the new names. This task was initially developed to rename 96 PDF files.

## Features

- Automatically reads an Excel file to extract old and new file names.
- Renames PDF files in bulk without manual intervention.
- Handles any number of files as long as the Excel file is formatted correctly.

## Requirements

- Python 3.x
- `pandas` library for handling Excel files
- `os` for interacting with the file system

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pdf-renaming-automation.git

2. Install the required libraries:
3. Ensure your Excel file (Temp.xlsx) is in the root directory, with columns:

Old Names: Contains the current PDF names.
New Names: Contains the new names for the PDF files.

## Usage
1. Place your PDFs in the pdf_files/ directory.
2. Make sure your Excel file (Temp.xlsx) is updated with the correct file names.
3. Run the Python script:
   ```bash
   python rename_pdfs.py
he script will rename the PDF files based on the data in the Excel sheet.

## Example
If Temp.xlsx contains:

Old Names   New Names
file1.pdf	  new_file1.pdf
file2.pdf	  new_file2.pdf
The script will rename file1.pdf to new_file1.pdf, and so on.



