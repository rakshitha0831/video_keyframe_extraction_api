import cv2
import os
import numpy as np
from datetime import timedelta


def extract_keyframes(video_path, output_dir, threshold=30):
    """
    Extract key frames from a video based on scene changes.
    
    Parameters:
        video_path (str): Path to the input video file.
        output_dir (str): Directory where key frames will be saved.
        threshold (int): Sensitivity for scene change detection (default = 30).
    
    Returns:
        list of tuples: [(filename, timestamp), ...]
    """
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise IOError(f"Cannot open video file: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS)
    success, prev_frame = cap.read()
    if not success:
        raise ValueError("Could not read first frame of video.")

    frame_id = 0
    keyframes, timestamps = [], []

    while True:
        success, frame = cap.read()
        if not success:
            break

        gray_diff = cv2.absdiff(
            cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY),
            cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        )
        diff_score = np.count_nonzero(gray_diff)

        if diff_score > threshold * 1000:
            timestamp = str(timedelta(seconds=frame_id / fps))
            frame_name = f"keyframe_{len(keyframes) + 1}.jpg"
            cv2.imwrite(os.path.join(output_dir, frame_name), frame)
            keyframes.append(frame_name)
            timestamps.append(timestamp)

        prev_frame = frame
        frame_id += 1

    cap.release()
    return list(zip(keyframes, timestamps))
