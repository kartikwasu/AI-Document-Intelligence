
import json
from pathlib import Path

def chunk_text(text, chunk_size=500, overlap=100):

    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("Overlap must be smaller than chunk size.")

    chunks = []

    start = 0

    while start < len(text):

        end = min(start + chunk_size, len(text))

        # Try to end at a word boundary
        if end < len(text):

            boundary = text.rfind(
                " ",
                start + int(chunk_size * 0.7),
                end
            )

            if boundary > start:
                end = boundary

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= len(text):
            break

        start = max(end - overlap, start + 1)

    return chunks

if __name__ == "__main__":

    input_path = Path("data/processed/cleaned_text.txt")

    output_path = Path("data/processed/chunks.json")

    try:

        text = input_path.read_text(encoding="utf-8")

        chunks = chunk_text(
            text,
            chunk_size=500,
            overlap=100
        )

        chunk_data = []

        for index, chunk in enumerate(chunks, start=1):

            chunk_data.append({
                "chunk_id": index,
                "text": chunk
            })

        output_path.write_text(
            json.dumps(chunk_data, indent=4, ensure_ascii=False),
            encoding="utf-8"
        )

        print("Text chunking completed successfully!")

        print("Total chunks:", len(chunks))

        print("Chunks saved at:", output_path)

        if chunks:
            print("\nFirst chunk preview:")
            print(chunks[0])

    except FileNotFoundError:

        print("Error: Cleaned text file not found.")

    except Exception as e:

        print("Error:", e)