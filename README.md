Real-Time Face Detection Using Python and OpenCV










A lightweight and efficient real-time face detection system built with Python and OpenCV.
The script uses the Haar Cascade model to detect faces from a live webcam feed and draw bounding boxes around them.
This repository is aimed at learners, hobbyists, and developers exploring computer vision fundamentals.

Features

Real-time face detection from your webcam

Haar Cascade frontal face classifier

Simple and clean codebase

Efficient grayscale processing

Bounding box overlays for detected faces

Safe exit using the A key or ESC

Demo (Screenshot Placeholder)

Add your screenshot here

📸 sample_output.jpg

Installation
1. Clone the repository
git clone https://github.com/your-username/opencv-face-detection.git
cd opencv-face-detection

2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate       # macOS / Linux
venv\Scripts\activate          # Windows

3. Install dependencies
pip install -r requirements.txt

Usage

Run the script:

python main.py


Exit keys:

Press A

Or press ESC

Requirements
opencv-python>=4.9.0
numpy>=1.24.0

Project Structure
📁 opencv-face-detection/
│── main.py
│── requirements.txt
│── LICENSE
│── README.md
│── samples/  (optional)

How It Works

A webcam frame is captured using OpenCV.

The frame is converted to grayscale for faster Haar Cascade processing.

The cascade classifier scans the image for faces.

Each detected face is outlined with a bounding box.

The loop continues until the user exits pressing A or ESC.

Future Enhancements

Face recognition (LBPH / DNN)

Emotion detection

Attendance system module

Dataset collection tool

Save snapshots of detected faces

License

This project is licensed under the MIT License.
Read the full license here:
MIT License

Contributions

Contributions are welcome.
You can fork the project, create a new branch, and open a pull request with improvements.

Acknowledgment

Built using Python, OpenCV, and the classic Haar Cascade model.
