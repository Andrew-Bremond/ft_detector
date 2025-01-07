import process_video
import alphapose_processing  
import os

def main():
    print("Choose pose detection library:")
    print("1. MediaPipe")
    print("2. AlphaPose")
    library_choice = input("Enter your choice (1 or 2): ")

    if library_choice not in ["1", "2"]:
        print("Invalid choice! Please enter 1 or 2.")
        return

    print("Choose input type:")
    print("1. Live video (webcam)")
    print("2. Pre-recorded video")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        if library_choice == '1':
            process_video.live_video_tracking()
        elif library_choice == '2':
            alphapose_processing.live_video_tracking()
    elif choice == '2':
        print("Choose a pre-recorded video:")
        print("1. slr_video_1.mp4")
        print("2. slr_video_2.mp4")
        print("3. slr_video_3.mp4")
        video_choice = input("Enter the number of your choice (1, 2, or 3): ")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        video_map = {
            "1": os.path.join(base_dir, "../data/videos/slr_video_1.mp4"),
            "2": os.path.join(base_dir, "../data/videos/slr_video_2.mp4"),
            "3": os.path.join(base_dir, "../data/videos/slr_video_3.mp4"),
        }

        video_path = video_map.get(video_choice)
        if video_path:
            if not os.path.exists(video_path):
                print(f"Error: Video file not found at {video_path}. Please check the path.")
                return
            if library_choice == '1':
                process_video.process_video(video_path)
            elif library_choice == '2':
                alphapose_processing.process_video(video_path)
        else:
            print("Invalid choice! Please select a valid video.")
    else:
        print("Invalid choice! Please enter 1 or 2.")

if __name__ == '__main__':
    main()
