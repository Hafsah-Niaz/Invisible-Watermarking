from cryptography.fernet import Fernet
from PyPDF2 import PdfReader, PdfWriter
from docx import Document
import os

# Generate encryption key (should be fixed & securely stored in real apps)
key = Fernet.generate_key()
cipher = Fernet(key)

# ----------------- PDF Watermarking -----------------
def add_watermark_pdf(input_path, watermark_text, output_path):
    encrypted = cipher.encrypt(watermark_text.encode()).decode()
    reader = PdfReader(input_path)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    metadata = reader.metadata or {}
    metadata.update({"/Watermark": encrypted})
    writer.add_metadata(metadata)

    with open(output_path, "wb") as f:
        writer.write(f)

def trace_watermark_pdf(input_path):
    try:
        reader = PdfReader(input_path)
        metadata = reader.metadata
        encrypted = metadata.get("/Watermark", None)
        
        if encrypted:
            return cipher.decrypt(encrypted.encode()).decode()
        return "No watermark found."
    except Exception as e:
        return f"Error: {str(e)}"


# ----------------- Dispatcher -----------------
def add_watermark(input_path, watermark_text, output_path):
    ext = os.path.splitext(input_path)[1].lower()
    if ext == '.pdf':
        add_watermark_pdf(input_path, watermark_text, output_path)
   
    else:
        raise ValueError("Unsupported file type.")

def trace_watermark(input_path):
    ext = os.path.splitext(input_path)[1].lower()
    if ext == '.pdf':
        return trace_watermark_pdf(input_path)
   
    else:
        return "Unsupported file type."
