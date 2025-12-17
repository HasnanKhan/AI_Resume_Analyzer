# AI_Resume_Analyzer

AI-powered PDF resume/CV summarizer built with **Python**, **PyPDF2**, and the **OpenAI API**.  
Point it at a PDF and it will extract the text, split long documents into chunks, summarize each chunk, and produce a final concise summary.

## Features
- Extracts text from **PDF** files using **PyPDF2**
- Handles long resumes/CVs by **chunking** text (default: 4000 characters-ish by word sizing)
- Summarizes with **OpenAI Chat Completions**
- CLI options for:
  - max summary length (words)
  - chunk size
  - output to a file
  - API key via flag or environment variable

## Tech Stack
- **Python 3**
- **PyPDF2**
- **OpenAI Python SDK**
- **python-dotenv** for `.env` support

---

## Project Structure (typical)
```txt
AI_Resume_Analyzer/
  main.py
  .env (not committed)
  requirements.txt
If your file isn’t named main.py, just replace it in the commands below.

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
If you don’t have a requirements.txt yet, here’s a good one:

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
The script loads environment variables with:

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
