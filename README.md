README.md
PDF Text Extractor API
Overview
This project is a backend API built using FastAPI.
It allows users to upload a PDF file, extracts the first 200 characters from it, and returns the result in a structured JSON response.

The API also validates the uploaded file and handles errors like invalid file type, empty files, or no file uploaded.




Features
Accepts PDF files only

Handles empty or null files

Extracts text from PDF documents

Returns first 200 characters only

Provides a structured JSON response

Handles errors gracefully



How It Works
User uploads a PDF file

API checks the file type to ensure it is a PDF

API checks if the file is empty or contains no readable text

Extracts text from the PDF

Returns the first 200 characters

Sends a structured JSON response





API Endpoint
POST /upload-pdf

Form Field: file (PDF file)

Response Example (Success):

JSON

{
  "success": true,
  "message": "File processed successfully",
  "preview_text": "First 200 characters of extracted text..."
}
Error Examples:

JSON

{
  "success": false,
  "message": "Only PDF files are allowed"
}
JSON

{
  "success": false,
  "message": "Uploaded PDF is empty"
}
Technologies Used
Python

FastAPI – Backend framework

Uvicorn – ASGI server

PyPDF2 – PDF text extraction library

How to Run
Install dependencies:

Bash

pip install fastapi uvicorn PyPDF2 python-multipart
Run the server:

Bash

uvicorn main:app --reload
Open the browser:

Code

http://127.0.0.1:8000/docs
Use the Swagger UI to upload a PDF and test the API.
