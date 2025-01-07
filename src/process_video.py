import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

def live_video_tracking():
    cap = cv2.VideoCapture(0)  # Use webcam
    with mp_pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        smooth_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose:
        while True:
            success, frame = cap.read()
            if not success:
                break

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_frame)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                # Extract foot landmarks (for example, left foot index)
                left_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
                # You can use these coordinates to determine movement or position

            cv2.imshow('Live Foot Tracking', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cap.release()
    cv2.destroyAllWindows()

def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    prev_left_foot_y = None
    prev_right_foot_y = None
    threshold = 0.05  # Adjust threshold as needed

    with mp_pose.Pose(
        static_image_mode=False,
        model_complexity=1,
        smooth_landmarks=True,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5
    ) as pose:
        frame_count = 0

        while True:
            success, frame = cap.read()
            if not success:
                break
            frame_count += 1

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(rgb_frame)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                left_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_FOOT_INDEX]
                right_foot_index = results.pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX]

                current_left_foot_y = left_foot_index.y
                current_right_foot_y = right_foot_index.y

                if prev_left_foot_y is not None:
                    if prev_left_foot_y - current_left_foot_y > threshold:
                        print(f"[Frame {frame_count}] Left foot is being raised!")

                if prev_right_foot_y is not None:
                    if prev_right_foot_y - current_right_foot_y > threshold:
                        print(f"[Frame {frame_count}] Right foot is being raised!")

                prev_left_foot_y = current_left_foot_y
                prev_right_foot_y = current_right_foot_y

            cv2.imshow('Video Foot Tracking', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()
