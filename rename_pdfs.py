
### Python Script (`rename_pdfs.py`)

Here’s the Python code you can upload to GitHub:

```python
import os
import pandas as pd

# Load Excel file with old and new names
excel_file = 'Temp.xlsx'
df = pd.read_excel(excel_file)

# Directory containing the PDF files
pdf_directory = 'pdf_files/'

# Renaming process
for index, row in df.iterrows():
    old_name = row['Old Names']
    new_name = row['New Names']

    # Construct full paths
    old_file_path = os.path.join(pdf_directory, old_name)
    new_file_path = os.path.join(pdf_directory, new_name)

    # Rename the file
    if os.path.exists(old_file_path):
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {old_name} to {new_name}')
    else:
        print(f'File not found: {old_name}')
