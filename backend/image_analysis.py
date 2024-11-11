
from PIL import Image
from io import BytesIO
from text_analysis import analyze_text
import pytesseract

def analyze_image(image_bytes: bytes):
    image = Image.open(BytesIO(image_bytes))
    extracted_text = pytesseract.image_to_string(image)
    analysis_result = analyze_text(extracted_text)
    return {"extracted_text": extracted_text, "analysis_result": analysis_result}
