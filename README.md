🏋️ Dip Counter using MediaPipe & OpenCV
This is a Machine Learning-based computer vision project that automatically counts "dips" (tricep dips) using MediaPipe and OpenCV in Python. The project leverages pose estimation to detect upper body movement and tracks repetitions in real-time, making it ideal for fitness applications or personal workout tracking.

🎯 Project Objective
To create a lightweight and efficient exercise tracking system that:
Uses a webcam feed to monitor user movement
Detects dips using pose landmarks from MediaPipe
Counts each completed dip rep accurately

🛠️ Tech Stack
Python
MediaPipe 
OpenCV 
NumPy

📸 How It Works
Captures live video using your webcam.
Detects and tracks pose landmarks (e.g., shoulders, elbows, hips).
Calculates angles to determine the dip position.
Counts a rep each time the full dip motion is completed.
Displays the count.

💡 Use Case
Perfect for:
Home workouts
Fitness apps
Personal training
