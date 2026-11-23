
from pypdf import PdfReader


def extract_pdf_text(pdf_path):

    reader = PdfReader(pdf_path)

    extracted_text = ""

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text:
            extracted_text += f"\n--- Page {page_number} ---\n"
            extracted_text += text

    return extracted_text


if __name__ == "__main__":

    pdf_path = "data/uploads/sample.pdf"

    text = extract_pdf_text(pdf_path)

    if text.strip():
        print("PDF text extracted successfully!")
        print(text)
    else:
        print("No readable text found in this PDF.")
