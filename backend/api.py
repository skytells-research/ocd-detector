
from fastapi import FastAPI, UploadFile, File, HTTPException
from text_analysis import analyze_text, analyze_with_openai
from image_analysis import analyze_image
from voice_analysis import analyze_voice
from model_training import train_model

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the enhanced OCD Detector API"}

@app.post("/analyze/text")
def analyze_text_endpoint(data: dict):
    chat_text = data.get('chat_text', '')
    if not chat_text:
        raise HTTPException(status_code=400, detail="No text provided for analysis.")
    result = analyze_text(chat_text)
    return {"text_analysis": result}

@app.post("/analyze/image")
async def analyze_image_endpoint(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = analyze_image(contents)
        return {"image_analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze/voice")
async def analyze_voice_endpoint(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        result = analyze_voice(contents)
        return {"voice_analysis": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/train")
def train_model_endpoint(train_file: str, test_file: str):
    if not train_file or not test_file:
        raise HTTPException(status_code=400, detail="Training and testing file paths are required.")
    try:
        train_model(train_file, test_file)
        return {"message": "Model training completed successfully."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health_check():
    """Return system health status."""
    import psutil
    import time

    health_status = {
        "status": "healthy",
        "uptime": f"{time.time() - psutil.boot_time():.2f} seconds",
        "cpu_usage": f"{psutil.cpu_percent()}%",
        "memory_usage": f"{psutil.virtual_memory().percent}%",
    }
    return health_status
