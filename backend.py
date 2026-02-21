from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
import uuid
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload-logo")
async def upload_logo(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    file_path = f"{UPLOAD_DIR}/{file_id}_{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "Logo uploaded successfully", "file_path": file_path}

@app.post("/generate-brand-identity")
async def generate_brand_identity(
    brand_name: str = Form(...),
    industry: str = Form(...),
    tone: str = Form(...)
):
    brand_identity = {
        "brand_name": brand_name,
        "industry": industry,
        "tone": tone,
        "logo_idea": f"Minimal modern logo for {brand_name}",
        "color_palette": ["#000000", "#FFFFFF", "#FF5733"],
        "font_style": "Sans-serif"
    }
    return brand_identity

@app.post("/generate-content")
async def generate_content(
    brand_name: str = Form(...),
    content_type: str = Form(...)
):
    content = {
        "brand_name": brand_name,
        "content_type": content_type,
        "text": f"This is AI-generated {content_type} content for {brand_name}"
    }
    return content

@app.get("/")
def home():
    return {"status": "BrandCraft Backend Running"}