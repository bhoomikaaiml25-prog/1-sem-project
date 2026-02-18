import pytesseract
from PIL import Image
import google.generativeai as genai

def analyze_report(image_path):
  #Step 1: Extract text using OCR
  img = Image.open(image_parh)
  extracted_text = pytesseract.image_to_string(img)

#Step 2: Send to AI fir summary
model = genai.GenerativeModel('gemini-pro')
prompt = f" Analyze thos medical report and summarize it for a patient:{extra 
response = model generate_content(prompt)

return response.text
