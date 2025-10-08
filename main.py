from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import shutil
import os
from keyframe_extractor import extract_keyframes

# --- App Configuration ---
app = FastAPI(
    title="Video Keyframe Extraction API",
    description="Uploads a video and returns key frames with timestamps.",
    version="1.0"
)

UPLOAD_FOLDER = "sample_videos"
OUTPUT_FOLDER = "outputs"

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Mount the outputs folder to serve images
app.mount("/outputs", StaticFiles(directory=OUTPUT_FOLDER), name="outputs")


# --- Root Route ---
@app.get("/")
def home():
    """
    Root endpoint for the API.
    """
    return {
        "message": "Welcome to the Video Keyframe Extraction API. "
                   "Use /docs to upload a video and extract key frames."
    }


# --- Endpoint 1: Upload and Extract Keyframes ---
@app.post("/extract_keyframes/")
async def extract_keyframes_endpoint(file: UploadFile = File(...)):
    """
    Uploads a video and extracts key frames based on scene changes.
    """
    # Validate file type
    if not file.filename.lower().endswith((".mp4", ".mov")):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload an MP4 or MOV video.")

    # Save uploaded video
    video_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Run keyframe extraction
    try:
        results = extract_keyframes(video_path, OUTPUT_FOLDER)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing video: {str(e)}")

    # Prepare response
    response = {
        "video": file.filename,
        "keyframes_extracted": len(results),
        "frames": [{"file": name, "timestamp": ts} for name, ts in results]
    }

    return response


# --- Endpoint 2: Preview Extracted Keyframes ---
@app.get("/preview", response_class=HTMLResponse)
def preview_keyframes():
    """
    Displays extracted keyframes as an HTML gallery in the browser.
    """
    images = [f for f in os.listdir(OUTPUT_FOLDER) if f.endswith(".jpg")]
    if not images:
        return "<h3>No keyframes found. Please run extraction first.</h3>"

    html_content = """
    <html>
    <head>
        <title>Keyframe Preview</title>
    </head>
    <body style='text-align:center; font-family:Arial'>
        <h2>🎞 Extracted Keyframes Preview</h2>
        <div style='display:flex; flex-wrap:wrap; justify-content:center;'>
    """

    for img in images:
        html_content += f"""
        <div style='margin:10px;'>
            <img src='/outputs/{img}' width='220'
                 style='border-radius:8px; box-shadow:0 0 5px gray;'>
            <p>{img}</p>
        </div>
        """

    html_content += "</div></body></html>"

    return html_content
