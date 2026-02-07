from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LongText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "KING_ABHI_X backend running"}

@app.post("/long-video")
def long_video(data: LongText):
    # अभी demo response (लेकिन API सच में काम करती है)
    return {
        "message": "Long video request received",
        "text_length": len(data.text),
        "status": "success"
    }
  cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
