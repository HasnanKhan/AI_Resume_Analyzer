# AI_Resume_Analyzer

AI-powered PDF resume/CV summarizer built with **Python**, **PyPDF2**, and the **OpenAI API**.  
Point it at a PDF and it will extract the text, split long documents into chunks, summarize each chunk, and produce a final concise summary.

---

## Features

- Extracts text from **PDF** files using **PyPDF2**
- Handles long resumes/CVs by **chunking** text (default: 4000 chars-ish by word sizing)
- Summarizes with **OpenAI Chat Completions**
- CLI options for:
  - max summary length (words)
  - chunk size
  - output to a file
  - API key via flag or environment variable

---

## Tech Stack

- **Python 3**
- **PyPDF2**
- **OpenAI Python SDK**
- **python-dotenv** for `.env` support

---

## Project Structure (typical)


AI_Resume_Analyzer/
  main.py
  .env (not committed)
  requirements.txt
If your file isn’t named main.py, replace it in the commands below.

Setup
1) Clone the repo
bash
Copy code
git clone https://github.com/<your-username>/AI_Resume_Analyzer.git
cd AI_Resume_Analyzer
2) Create and activate a virtual environment (recommended)
bash
Copy code
python -m venv .venv

# macOS/Linux
source .venv/bin/activate

# Windows
# .venv\Scripts\activate
3) Install dependencies
bash
Copy code
pip install -r requirements.txt
If you don’t have a requirements.txt yet, here’s a solid starter:

txt
Copy code
openai
PyPDF2
python-dotenv
Environment Variables
Create a .env file in the project root:

env
Copy code
OPENAI_API_KEY=your_api_key_here
The script loads env vars using:

load_dotenv(override=True)

looks for OPENAI_API_KEY

Usage
Basic (prints summary to terminal)
bash
Copy code
python main.py /path/to/resume.pdf
Set max summary length (words)
bash
Copy code
python main.py /path/to/resume.pdf --max-length 150
Change chunk size
bash
Copy code
python main.py /path/to/resume.pdf --chunk-size 3500
Save output to a file
bash
Copy code
python main.py /path/to/resume.pdf --output summary.txt
Provide API key via CLI (optional)
bash
Copy code
python main.py /path/to/resume.pdf --api-key YOUR_KEY_HERE
Example Output
The tool prints progress logs and then a final section like:

SUMMARY

summary text

an optional “saved to” line if --output is provided

Notes / Limitations
Scanned PDFs (image-only resumes) may extract little or no text using PyPDF2. If you need scanned support, add OCR (e.g., Tesseract) before summarization.

Quality depends on the extracted text and the model.

Large PDFs may take longer and use more tokens due to chunking + multiple calls.

Configuration
Default CLI values:

--max-length: 200 (words)

--chunk-size: 4000

You can tweak these depending on how detailed you want the summary.

Security
Do not commit your .env file.

Add this to .gitignore:

txt
Copy code
.env
.venv/
__pycache__/
Roadmap Ideas (optional)
Resume-specific structured output (skills, experience, education, projects)

Scoring against a job description (match %, missing keywords)

PDF upload + web UI (Streamlit/Flask)

OCR support for scanned PDFs

License
MIT (or your preferred license)

Copy code






