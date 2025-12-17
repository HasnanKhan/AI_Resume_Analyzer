AI_Resume_Analyzer

AI-powered PDF resume/CV summarizer built with Python, PyPDF2, and the OpenAI API.

Extracts text from a PDF, chunks long documents, summarizes each chunk, then produces a clean final summary you can print or save.

✨ What it does

✅ Extracts text from PDFs using PyPDF2

✅ Handles long PDFs with chunking

✅ Summarizes using OpenAI Chat Completions

✅ Simple CLI with flags for output + length + chunk size

🧰 Tech Stack

Python

PyPDF2

OpenAI Python SDK

python-dotenv

📁 Project Structure
AI_Resume_Analyzer/
  main.py            # (or your script file)
  requirements.txt
  .env               # not committed


If your script file isn’t named main.py, replace it in the commands below.

⚡ Quickstart
1) Clone
git clone https://github.com/<your-username>/AI_Resume_Analyzer.git
cd AI_Resume_Analyzer

2) Create a virtual environment (recommended)
python -m venv .venv


Activate it:

macOS/Linux

source .venv/bin/activate


Windows

.venv\Scripts\activate

3) Install dependencies
pip install -r requirements.txt


If you don’t have a requirements.txt yet, use this:

openai
PyPDF2
python-dotenv

🔐 Setup your OpenAI API key

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here


This project loads it with:

load_dotenv(override=True)

reads OPENAI_API_KEY

▶️ Usage
Basic (prints summary to terminal)
python main.py /path/to/resume.pdf

Set max summary length (words)
python main.py /path/to/resume.pdf --max-length 150

Change chunk size
python main.py /path/to/resume.pdf --chunk-size 3500

Save summary to a file
python main.py /path/to/resume.pdf --output summary.txt

Provide API key via CLI (optional)
python main.py /path/to/resume.pdf --api-key YOUR_KEY_HERE

🧾 CLI Options

pdf_path (required): Path to the PDF file

-l, --max-length (default: 200): Max summary length in words

-c, --chunk-size (default: 4000): Chunk size used for large PDFs

-o, --output (optional): Write summary to a file

--api-key (optional): OpenAI API key (otherwise uses OPENAI_API_KEY)

🧠 How it works (high-level)

Extracts all text from the PDF

If text is short: summarize directly

If text is long: split into chunks → summarize each chunk

Combine chunk summaries → optionally summarize again for a final result

⚠️ Notes / Limitations

Scanned/image-only PDFs may return no text with PyPDF2. For those, you’ll need OCR (e.g., Tesseract) before summarizing.

Summary quality depends on the extracted text (formatting-heavy PDFs can extract messy text).

The model is currently set in code to:

model="gpt-3.5-turbo"

You can swap the model name in summarize_chunk().

🔒 Security

Add this to .gitignore to avoid leaking secrets:

.env
.venv/
__pycache__/


Never commit your API key.

🗺️ Roadmap (optional ideas)

Structured resume output (Skills / Experience / Education / Projects)

Score resume vs job description (match %, missing keywords)

OCR support for scanned PDFs

Simple UI (Streamlit/Flask)

📄 License

MIT (or your preferred license)
