 Project Overview
 
 AirCanvas is a real-time Computer Vision application that transforms your webcam into a digital canvas. By leveraging advanced hand-tracking algorithms, users can draw, select colors, and interact with a virtual interface using only hand gestures—no mouse, touch-pad, or physical hardware required.This project demonstrates the practical application of Human-Computer Interaction (HCI) and real-time image processing pipelines.
 
 Key FeaturesTouchless Drawing:
 
 Use your index finger as a virtual pen with sub-millisecond tracking.
 
 Intuitive Gestures: - 
 
 One Finger Up: Drawing Mode.
 
 Two Fingers Up: Selection/Hover Mode (to change colors or clear screen).
 
 Modular Architecture: Clean, object-oriented code split into specialized modules for tracking and UI.
 
 Visual Feedback: Real-time on-screen HUD (Heads-Up Display) for color selection.
 
 Technical Stack & ConceptsPython: The core programming language.
 
 OpenCV: Handles video stream processing, bitwise operations for the canvas, and UI rendering.
 
 MediaPipe: Utilizes a pre-trained Palm Detection and Hand Landmark model to identify 21 3D coordinates on the hand.
 
 NumPy: Used for high-performance matrix manipulation of the digital drawing layers.
 
 Project StructurePlaintextAirCanvas-CV/

├── src/

│   ├── __init__.py

│   ├── hand_tracking.py   # HandDetector class (Computer Vision logic)

│   └── ui_manager.py      # UIManager class (Canvas & UI logic)

├── app.py                 # Main Entry Point

├── requirements.txt       # Project Dependencies

└── README.md              # Documentation

Installation & SetupFollow these steps to get the project running on your local machine:

Clone the RepositoryBashgit clone https://github.com/your-username/AirCanvas-CV.git

cd AirCanvas-CV

Create a Virtual Environment (Optional but Recommended)

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate

Install DependenciesBashpip

install -r requirements.txt

Launch the Application

python app.py

How to UseCalibrate: Position yourself so your hand is clearly visible to the webcam.
Select Color: Raise your Index and Middle fingers. Move your hand to the top of the screen and hover over a color block.

Draw: Raise only your Index finger. Move it around the screen to begin drawing.

Clear Canvas: In Selection Mode (two fingers), hover over the white "CLEAR" button at the top right.

Exit: Press the 'q' key on your keyboard to close the application.

Reflection & LearningThe Jitter Problem: Initial tracking was shaky. I resolved this by implementing a coordinate smoothing logic where the drawing only occurs when the landmark detection confidence exceeds 85%.

Layer Merging: A significant challenge was overlaying a transparent drawing on a live BGR video feed. I solved this using Inverse Masking (cv2.bitwise) to "cut out" the drawing space from the video frame before adding the colored pixels.
