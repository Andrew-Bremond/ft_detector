import cv2
import os
import subprocess

def run_alphapose(input_path, output_dir):
    # Ensure AlphaPose's inference script is accessible
    alphapose_command = [
        "python",
        "scripts/demo_inference.py",  # Change this path based on your AlphaPose setup
        "--detector",
        "yolo",  # Default AlphaPose detector
        "--video",
        input_path,
        "--outdir",
        output_dir
    ]
    subprocess.run(alphapose_command, check=True)

def live_video_tracking():
    print("AlphaPose live tracking is not natively supported for webcams.")
    print("Consider capturing the live feed and processing it as a video file.")

def process_video(video_path):
    # Prepare output directory
    output_dir = os.path.join("alphapose_output")
    os.makedirs(output_dir, exist_ok=True)

    print(f"Running AlphaPose on video: {video_path}")
    try:
        run_alphapose(video_path, output_dir)
        print(f"AlphaPose output saved in {output_dir}")
    except Exception as e:
        print(f"Error running AlphaPose: {e}")
