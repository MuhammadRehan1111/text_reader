from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PyPDF2 import PdfReader
import io

app = FastAPI()

# -----------------------------
# Structured Response Functions
# -----------------------------

def success_response(message, data):
    return {
        "status": "success",
        "code": 200,
        "message": message,
        "data": data
    }

def error_response(message, code):
    return JSONResponse(
        status_code=code,
        content={
            "status": "error",
            "code": code,
            "message": message,
            "data": None
        }
    )

# -----------------------------
# PDF Upload Endpoint
# -----------------------------

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):

    # 1️⃣ File Null Check
    if not file:
        return error_response("No file uploaded", 400)

    # 2️⃣ File Type Validation
    if file.content_type != "application/pdf":
        return error_response("Only PDF files are allowed", 400)

    try:
        content = await file.read()

        # 3️⃣ Empty File Check
        if len(content) == 0:
            return error_response("Uploaded PDF is empty", 400)

        # 4️⃣ File Size Limit (5MB)
        if len(content) > 5 * 1024 * 1024:
            return error_response("File size exceeds 5MB limit", 400)

        # 5️⃣ Read PDF
        pdf = PdfReader(io.BytesIO(content))

        # 6️⃣ Zero Page Check
        if len(pdf.pages) == 0:
            return error_response("PDF has no pages", 400)

        # 7️⃣ Encrypted PDF Check
        if pdf.is_encrypted:
            return error_response("Encrypted PDFs are not supported", 400)

        # 8️⃣ Extract Text
        text = ""
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted

        # 9️⃣ No Text Found (Scanned PDF)
        if not text.strip():
            return error_response(
                "No readable text found in PDF (possibly scanned document)",
                400
            )

        # 🔟 Get First 200 Characters
        preview = text.strip()[:200]

        return success_response(
            "PDF processed successfully",
            {
                "filename": file.filename,
                "preview": preview,
                "total_characters_extracted": len(text)
            }
        )

    except Exception:
        return error_response("Error processing PDF file", 500)