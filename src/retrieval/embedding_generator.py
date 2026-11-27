
import json
from pathlib import Path
from sentence_transformers import SentenceTransformer

def generate_embeddings(chunks):

    # Load pretrained embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Extract text from chunks
    texts = [chunk["text"] for chunk in chunks]

    # Generate embeddings
    embeddings = model.encode(
        texts,
        normalize_embeddings=True
    )

    return embeddings

if __name__ == "__main__":

    input_path = Path("data/processed/chunks.json")
    output_path = Path("data/processed/embeddings.json")

    try:

        # Read chunks
        with open(input_path, "r", encoding="utf-8") as file:
            chunks = json.load(file)

        if not chunks:
            print("No chunks found.")
            raise SystemExit

        print("Total chunks:", len(chunks))
        print("Loading embedding model...")

        # Generate embeddings
        embeddings = generate_embeddings(chunks)

        # Prepare output
        embedding_data = []

        for chunk, embedding in zip(chunks, embeddings):

            embedding_data.append({
                "chunk_id": chunk["chunk_id"],
                "text": chunk["text"],
                "embedding": embedding.tolist()
            })

        # Save embeddings
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(
                embedding_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Embeddings generated successfully!")
        print("Total embeddings:", len(embedding_data))
        print("Vector dimensions:", len(embeddings[0]))
        print("Saved at:", output_path)

    except FileNotFoundError:
        print("Error: chunks.json not found. Run text chunking first.")

    except Exception as e:
        print("Error while generating embeddings:", e)