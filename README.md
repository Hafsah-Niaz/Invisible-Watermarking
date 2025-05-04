# Invisible-Watermarking
# 🛡️ Invisible PDF Watermarking Website

This is a simple web application that allows you to:  
✅ Add an invisible watermark to PDF files  
✅ Trace and retrieve the watermark later  

**Built with:**
1. **Frontend:** HTML + CSS  
2. **Backend:** Python (Flask + PyPDF2 + Cryptography)

---

## 🚀 Features
1. Upload any **PDF file** and embed an encrypted invisible watermark.
2. Later, trace back the watermark to check ownership or source.
3. Watermark is stored securely in the **PDF metadata** (invisible to normal viewers).

---

## 📂 Project Structure
├── app.py # Flask application
├── watermark.py # Core logic for watermarking
├── templates/
│ ├── index.html # Upload page
│ └── result.html # Result display page
├── static/
│ ├── style.css # Custom CSS styling
├── uploads/ # Folder to store uploaded PDFs
├── processed/ # Folder to store processed PDFs
├── requirements.txt # Python dependencies
└── README.md # (This file)

---

## 🛠️ Tech Stack
1. **Frontend:** HTML5, CSS3  
2. **Backend:** Python 3, Flask, PyPDF2, Cryptography (Fernet encryption)

---

## 📄 Usage

### ✅ Add Watermark
1. Upload a PDF.
2. Enter your watermark text.
3. Click **"Add Watermark"** to download the watermarked PDF.

### 🔎 Trace Watermark
1. Upload a previously watermarked PDF.
2. Click **"Trace Watermark"** to reveal the embedded watermark text.

---

## 📚 How It Works (Backend Logic)
1. Watermark text is **encrypted** using **Fernet symmetric encryption**.
2. Encrypted watermark is embedded in the **PDF metadata** (`/Watermark` field).
3. Tracing decrypts the metadata field to retrieve the original text.

---
