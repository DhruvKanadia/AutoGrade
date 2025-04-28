# AutoGrade
📝 **Handwritten Text to Digital Text Converter**

AutoGrade is a full-stack web application that allows users to upload images or PDFs of handwritten text and converts them into machine-readable text using **Google Gemini 2.0 Flash**. The project leverages **React.js** for the frontend and **Node.js + Express** for the backend.

---

## 🚀 Features
- **Upload handwritten documents** (images or PDFs).
- **Extract text** using Google's Gemini 2.0 Flash OCR model.
- **View and download** the extracted text as `.txt` or `.pdf`.
- Supports **multiple pages** from PDFs.
- **Responsive** and user-friendly interface.
- Handles **errors** and shows **loading indicators** during processing.

---

## 🛠️ Tech Stack
### Frontend:
- **React.js**

### Backend:
- **Node.js**
- **Express**

### OCR Model:
- **Google Gemini 2.0 Flash**

### Other Libraries:
- **axios**: For HTTP requests.
- **multer**: For file uploads.
- **pdf-lib** or **pdf2pic**: For PDF to image conversion.
- **pdfkit**: For generating PDFs.
- **cors**, **dotenv**: For backend utilities.

---

## 📂 Project Structure
- **Frontend**: React.js application for the user interface.
- **Backend**: Node.js + Express server for handling API requests and processing files.
- **OCR Integration**: Google Gemini 2.0 Flash for text extraction.

---

## 📖 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AutoGrade.git
