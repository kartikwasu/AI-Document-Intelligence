# AI Document Intelligence & Enterprise Knowledge Assistant

## Project Overview
An AI-powered document assistant that allows users to upload documents and ask questions based on their content.

## Problem Statement
Organizations store large amounts of information in PDF documents. Finding relevant information manually is time-consuming. This project aims to simplify document search and question answering using Retrieval-Augmented Generation (RAG).

## Objectives
- Upload and process PDF documents.
- Extract text from normal and scanned PDF pages.
- Use OCR to extract text from images and scanned pages.
- Clean and preprocess extracted text.
- Divide text into smaller chunks.
- Generate embeddings.
- Store document vectors in a vector database.
- Retrieve relevant information using RAG.
- Generate answers using an LLM.
- Display answers with document references.

## Technology Stack
- Python
- LangChain
- Groq API
- ChromaDB
- PyMuPDF
- Tesseract OCR
- Pytesseract
- Pillow
- FastAPI
- Streamlit

## Project Progress

- **Day 1:** Initial project setup and GitHub configuration.
- **Day 2:** Created project folder structure and installed dependencies.
- **Day 3:** Implemented PDF text extraction and text file storage.
- **Day 4:** Implemented text cleaning and preprocessing.
- **Day 5:** Implemented text chunking with configurable chunk size and overlap.
- **Day 6:** Added OCR support for scanned PDF pages using Tesseract.
- Generated `extracted_text.txt`, `cleaned_text.txt`, and `chunks.json` for the document processing pipeline.

## Current Workflow
PDF Upload → Text Extraction / OCR → Text Cleaning → Text Chunking → Embeddings → ChromaDB → RAG → LLM Answer

## Future Enhancements
- Semantic search using vector embeddings.
- Persistent vector storage with ChromaDB.
- Context-aware question answering using Groq.
- Source references in generated answers.
- User-friendly Streamlit interface.
- FastAPI backend integration.