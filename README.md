📄 AI-Powered CV Reader with Python, PyPDF2, and OpenAI

An intelligent PDF summarization tool built with Python that extracts and summarizes content from CVs or resumes using OpenAI's GPT models. Designed to process large PDF documents, intelligently chunk text, and generate concise summaries — ideal for HR tech, recruiting platforms, or research tools.

📚 Table of Contents

Introduction

Features

Installation

Usage

Configuration

Examples

Dependencies

Troubleshooting

Contributors

License

🧠 Introduction

This project provides a command-line tool that:

Extracts text from a PDF file (e.g., resumes or CVs),

Splits the text into manageable chunks if necessary,

Uses OpenAI's GPT models (via API) to summarize each chunk,

Optionally combines and further condenses the summary for large documents.

It is ideal for use cases where you need a quick, readable summary of a candidate’s resume or any other PDF-based content.

🚀 Features

✅ Text extraction from PDF using PyPDF2

✅ Intelligent chunking for long documents

✅ Uses OpenAI GPT (gpt-3.5-turbo) to generate summaries

✅ Configurable summary length and chunk size

✅ Supports output to file

✅ .env support for secure API key management

💾 Installation

Clone the repository:

git clone https://github.com/yourusername/ai-cv-reader.git
cd ai-cv-reader


Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Set up your .env file:
Create a .env file in the root directory:

OPENAI_API_KEY=your_openai_api_key_here

⚙️ Usage
python main.py path/to/your_cv.pdf

Optional Arguments:
Flag	Description
-l, --max-length	Max summary length in words (default: 200)
-c, --chunk-size	Text chunk size for processing (default: 4000)
-o, --output	Output file path (e.g., summary.txt)
--api-key	Pass API key directly (overrides .env)
Example:
python main.py resume.pdf -l 300 -o resume_summary.txt

🛠 Configuration

API Key: Stored securely using python-dotenv
. You can either:

Set it in a .env file as OPENAI_API_KEY=your_key

Or pass it via --api-key on the command line.

Chunking: Automatically splits long text (over chunk_size characters) to prevent model token limits.

🧪 Examples

Example Command:

python main.py sample_cv.pdf -l 250


Output:

============================================================
SUMMARY
============================================================
Experienced software engineer with a strong background in AI, cloud...
============================================================

📦 Dependencies

PyPDF2

openai

python-dotenv

Python 3.7+

To install them manually:

pip install PyPDF2 openai python-dotenv

🐞 Troubleshooting

No text found in PDF: Some PDFs use image-based text. Use OCR tools like Tesseract for preprocessing.

API key errors: Ensure .env is correctly configured, or pass the --api-key flag.

Rate limits: If summarizing many large files, you may hit OpenAI's rate or usage limits.

👥 Contributors

Your Name – @yourgithub

Want to contribute? Feel free to open issues or submit pull requests.

📄 License

This project is licensed under the MIT License
.
