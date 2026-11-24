
import re
from pathlib import Path


def clean_text(text):

    # Remove unwanted control characters
    text = re.sub(r"[\x00-\x08\x0B-\x1F\x7F]", "", text)

    # Remove extra spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove spaces at the beginning and end
    text = text.strip()

    return text


if __name__ == "__main__":

    input_path = Path("data/processed/extracted_text.txt")

    output_path = Path("data/processed/cleaned_text.txt")

    try:

        text = input_path.read_text(encoding="utf-8")

        cleaned_text = clean_text(text)

        output_path.write_text(
            cleaned_text,
            encoding="utf-8"
        )

        print("Text cleaning completed successfully!")

        print("Cleaned text saved at:", output_path)

    except FileNotFoundError:

        print("Error: Extracted text file not found.")

    except Exception as e:

        print("Error:", e)
