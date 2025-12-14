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
