# PDF Splitter

This is a Python script that allows you to split a PDF file into multiple smaller PDF files. You can specify the range of pages to be extracted from the original PDF and save them as separate files.

## Usage

1. Install the required `PyPDF2` library by running the following command:
`pip install PyPDF2`

2. Copy the script into a Python environment or save it as a `.py` file.

3. Run the script and provide the following inputs:
- File path of the original PDF (including the extension)
- Name for the new split PDF files (without the extension)
- Start page number to split from (1-based index)
- End page number to stop the split at

4. The script will split the PDF into smaller files based on the specified page range.

## Notes

- Make sure to provide valid inputs, including the correct file path, start page, and end page.
- The script uses the `PyPDF2` library to read and manipulate PDF files.
- If you encounter any errors or need to modify the split parameters, the script will prompt you for the necessary information.
- The resulting split PDF files will be saved in the same directory as the script.

## Example

Here's an example usage of the script:

`Please enter file path with extension: example.pdf`
`Please enter split PDF name without extension: split`
`Please enter start page to split from: 3`
`Please enter the end page to stop the split at: 5`


This will split the `example.pdf` file starting from page 3 and ending at page 5. The resulting split PDF files will be named `split.pdf`.
