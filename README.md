# 🎥 Video Keyframe Extraction API

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)  ![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)  ![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?logo=opencv)  ![Uvicorn](https://img.shields.io/badge/Uvicorn-Server-orange)  ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

The **Video Keyframe Extraction API** is a computer vision project that automatically identifies and extracts  *key frames* , the most visually significant moments, from any uploaded video.

It demonstrates the use of  **scene change detection** ,  **frame difference analysis** , and **API deployment** using FastAPI and OpenCV.

The system processes videos frame by frame, detects major visual transitions, and outputs both **timestamped frames** and a **visual gallery** for easy inspection.

---

## Dataset / Input Details

* **Input Type:** Any `.mp4` or `.mov` video file
* **Output:** Extracted `.jpg` key frames and JSON metadata
* **Storage:** Saved locally under `outputs/`
* **Frame Analysis Method:** Pixel intensity difference using OpenCV
* **Threshold Parameter:** Adjustable for sensitivity control

---

## Pipeline Flow (End to End)

1. **Video Upload** – Upload `.mp4` or `.mov` files via the `/extract_keyframes/` endpoint.
2. **Frame Difference Computation** – Calculate pixel-wise intensity differences between consecutive frames.
3. **Scene Change Detection** – Detect abrupt scene changes using a configurable threshold.
4. **Key Frame Extraction** – Save frames representing major visual transitions with timestamps.
5. **Response Generation** – Return a structured JSON output listing each frame name and timestamp.
6. **Visual Preview** – Access `/preview` to view all extracted frames in an HTML gallery.

---

## API Endpoints

| Endpoint                | Method         | Description                                                                    |
| ----------------------- | -------------- | ------------------------------------------------------------------------------ |
| `/extract_keyframes/` | **POST** | Uploads a video and returns JSON metadata with extracted frames and timestamps |
| `/preview`            | **GET**  | Displays extracted key frames as a responsive gallery in the browser           |

---

## Technical Architecture

| Component                     | Technology   |
| ----------------------------- | ------------ |
| **Backend Framework**   | FastAPI      |
| **Video Processing**    | OpenCV       |
| **Computation**         | NumPy        |
| **Serving and Hosting** | Uvicorn      |
| **Language**            | Python 3.10+ |

---

## Example Workflow

1. **Run the API locally**

   ```bash
   uvicorn main:app --reload
   ```
2. **Open Swagger UI:**

   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
3. **Upload a video (for example, `sample-5s.mp4`)**
   Example JSON response:

   ```json
   {
     "video": "sample-5s.mp4",
     "keyframes_extracted": 5,
     "frames": [
       {"file": "keyframe_1.jpg", "timestamp": "0:00:02"},
       {"file": "keyframe_2.jpg", "timestamp": "0:00:04"}
     ]
   }
   ```
4. **Preview results visually:**

   [http://127.0.0.1:8000/preview](http://127.0.0.1:8000/preview)

---

## Visual Output Example

| Key Frame                                                 | Timestamp |
| --------------------------------------------------------- | --------- |
| ![Keyframe 1](https://chatgpt.com/c/outputs/keyframe_1.jpg) | 00:00:02  |
| ![Keyframe 2](https://chatgpt.com/c/outputs/keyframe_2.jpg) | 00:00:04  |
| ![Keyframe 3](https://chatgpt.com/c/outputs/keyframe_3.jpg) | 00:00:07  |

---

## Folder Structure

```
video_keyframe_extraction_api/
│
├── main.py                 # FastAPI app with endpoints
├── keyframe_extractor.py   # Frame extraction logic
├── sample_videos/          # Sample input videos
├── outputs/                # Extracted frames and timestamps
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## Installation and Setup

```bash
git clone <repo-url>
cd video_keyframe_extraction_api
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

Access locally at:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

👉 [http://127.0.0.1:8000/preview](http://127.0.0.1:8000/preview)

---

## 🚀 Deployment Guide

### 🖥️ Local Deployment (Recommended for Testing)

Run the following command from your project directory:

```bash
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

Then open your browser and go to:

```
http://localhost:8000/docs
```

### 🐳 Docker Deployment

You can easily containerize this API using Docker.

1. **Create a Dockerfile**
   ```dockerfile
   FROM python:3.10-slim
   WORKDIR /app
   COPY . .
   RUN pip install -r requirements.txt
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```
2. **Build and Run**
   ```bash
   docker build -t video-keyframe-api .
   docker run -d -p 8000:8000 video-keyframe-api
   ```

Visit:

```
http://localhost:8000/docs
```

### ☁️ Cloud Deployment (Optional)

You can deploy this project for free on:

* **Render** – One-click FastAPI deployment
* **Railway** – Simple containerized deployment
* **AWS EC2 / Lightsail** – Scalable production setup

---

## Tech Stack and Libraries

* **Languages:** Python 3.10+
* **Frameworks:** FastAPI, Uvicorn
* **Computer Vision:** OpenCV
* **Computation:** NumPy
* **Deployment:** Local, Docker, or Cloud-ready

---

## Use Cases

| Domain              | Application                                           |
| ------------------- | ----------------------------------------------------- |
| 🎬 Video Analytics  | Automatic highlight detection and scene summarization |
| 📊 Marketing and UX | Identify attention-grabbing ad segments               |
| 🔍 Research         | Detect visual transitions for attention tracking      |
| 🧠 AI Pipelines     | Preprocessing stage for visual summarization models   |

---

## Future Enhancements

* Integrate AI-based scene segmentation for smarter frame selection.
* Add support for batch video uploads.
* Implement frame clustering to reduce redundancy.
* Extend `/preview` with interactive playback timelines.
* Deploy to AWS EC2, GCP, or Azure App Services for production use.

---

## About the Author and Project Motivation

This project was developed by  **Rakshitha Venkatesh** , a Data Science enthusiast exploring practical applications of computer vision.

The **Video Keyframe Extraction API** was created as a compact, end-to-end example of how AI can automate video analysis and help identify important visual moments efficiently.

**Motivation:**

To build a simple, functional API that applies computer vision in a real-world setting and connects learning with hands-on implementation.

---

## Credits and Acknowledgements

Developed as part of a practical AI engineering showcase focusing on  **computer vision, backend APIs, and visual intelligence** .

Special thanks to open-source contributors of the **FastAPI** and **OpenCV** communities for their robust frameworks and documentation that made this implementation possible.
