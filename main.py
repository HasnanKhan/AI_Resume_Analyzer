#Build an AI powered CV Reader with Python -> PyPDF and OpenAI

import argparse
import os
import sys
from pathlib import Path
from typing import List, Optional
import PyPDF2
from openai import OpenAI

from dotenv import load_dotenv
load_dotenv(override=True)

#Main class to analyze PDF
class PDFSummarizer:
    def __init__(self, api_key: Optional[str] = None):
        """Initialize the PDF summarizer with OpenAI API key."""
        # Try to get API key from parameter, .env file, or environment
        api_key = api_key or os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=api_key)
        
        if not self.client.api_key:
            raise ValueError("OpenAI API key required. Set OPENAI_API_KEY in .env file or pass api_key parameter.")
    
    def extract_text(self, pdf_path: str) -> str:
        """Extract text from PDF file using PyPDF2."""
        try:
            pdf_file = Path(pdf_path)
            with open(pdf_file, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                return text.strip()
        except Exception as e:
            raise Exception(f"Error reading PDF: {e}")
    
    def chunk_text(self, text: str, chunk_size: int = 4000) -> List[str]:
        """Split text into chunks for processing large documents."""
        words = text.split()
        chunks = []
        current_chunk = []
        current_size = 0
        
        for word in words:
            # Check if adding this word would exceed chunk size
            if current_size + len(word) + 1 > chunk_size and current_chunk:
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]
                current_size = len(word)
            else:
                current_chunk.append(word)
                current_size += len(word) + 1
        
        # Don't forget the last chunk
        if current_chunk:
            chunks.append(" ".join(current_chunk))
        
        return chunks
    
    def summarize_chunk(self, chunk: str, max_length: int = 200) -> str:
        """Summarize a single text chunk using OpenAI GPT."""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system", 
                        "content": f"Summarize the following text in {max_length} words or less. Focus on key points and main ideas:"
                    },
                    {"role": "user", "content": chunk}
                ],
                max_tokens=300,
                temperature=0.3
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error summarizing chunk: {e}"
    
    def summarize_pdf(self, pdf_path: str, max_length: int = 200, chunk_size: int = 4000) -> str:
        """Summarize entire PDF document."""
        print(f"Extracting text from {pdf_path}...")
        text = self.extract_text(pdf_path)
        
        if not text.strip():
            return "No text found in PDF."
        
        print(f"Text extracted ({len(text)} characters)")
        
        # For short documents, summarize directly
        if len(text) <= chunk_size:
            print("Summarizing directly...")
            return self.summarize_chunk(text, max_length)
        
        # For longer documents, break into chunks
        print(f"Breaking text into manageable chunks...")
        chunks = self.chunk_text(text, chunk_size)
        print(f"Created {len(chunks)} chunks")
        
        summaries = []
        for i, chunk in enumerate(chunks, 1):
            print(f"Summarizing chunk {i}/{len(chunks)}...")
            # Distribute max_length across chunks
            chunk_max_length = max_length // len(chunks)
            summary = self.summarize_chunk(chunk, chunk_max_length)
            summaries.append(summary)
        
        # Combine all chunk summaries
        combined_summary = " ".join(summaries)
        
        # If combined summary is still too long, summarize it again
        if len(combined_summary) > max_length:
            print("Creating final summary...")
            return self.summarize_chunk(combined_summary, max_length)
        
        return combined_summary

def main():
    parser = argparse.ArgumentParser(description="AI-Powered PDF Summarizer")
    parser.add_argument("pdf_path", help="Path to PDF file")
    parser.add_argument("-l", "--max-length", type=int, default=200, 
                       help="Maximum summary length in words (default: 200)")
    parser.add_argument("-c", "--chunk-size", type=int, default=4000,
                       help="Text chunk size for processing (default: 4000)")
    parser.add_argument("-o", "--output", help="Output file path (optional)")
    parser.add_argument("--api-key", help="OpenAI API key (or set OPENAI_API_KEY env var)")
    
    args = parser.parse_args()
    
    # Check if PDF file exists
    pdf_file = Path(args.pdf_path)
    if not pdf_file.exists():
        print(f"Error: PDF file '{args.pdf_path}' not found.")
        sys.exit(1)
    
    try:
        print("Starting PDF summarization...")
        summarizer = PDFSummarizer(api_key=args.api_key)
        
        summary = summarizer.summarize_pdf(
            args.pdf_path, 
            max_length=args.max_length,
            chunk_size=args.chunk_size
        )
        
        # Display results
        print("\n" + "="*60)
        print("SUMMARY")
        print("="*60)
        print(summary)
        print("="*60)
        
        # Save to file if requested
        if args.output:
            output_file = Path(args.output)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(summary)
            print(f"\nSummary saved to: {args.output}")
        
        print("\nSummarization complete!")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()