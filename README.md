# 1-sem-project
project tile : AI medical scan
code
import pytesseract
from PIL import Image
import google.generativeai as genai

def analyze_report(image_path):
#step 1: Extract text using OCR
img = Image.open(image.path)
extracted_text = pytesseract.image_to_string(img)

#step 2:send to AI for summary
model = genai.GenerativeModel('gemini-pro')
prompt = f"Analyze this medical report and summarize it for a patient: {extra }
response = model.generate_content(prompt)

return response.text
