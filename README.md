# Virtual Cursor Control

## Overview

Virtual Cursor Control is an AI-powered system that allows users to control their computer cursor using hand gestures captured by a webcam. This project aims to provide an alternative to traditional mouse devices, making computer interaction more accessible and touch-free.

## Features

- Control cursor movement using hand gestures
- Perform left-click operations
- No additional hardware required beyond a standard webcam
- High accuracy (99%) in gesture recognition

## Technologies Used

- Python
- OpenCV
- MediaPipe
- AutoPy

## How It Works

1. The system captures video input from the computer's webcam.
2. Hand landmarks are detected using the MediaPipe framework.
3. Specific hand gestures are interpreted as mouse commands:
   - Moving index finger: Move cursor
   - Index and middle fingers together: Left-click
   - All fingers up: No action

## Installation

1. Clone this repository:


```bash
git clone https://github.com/diaz3z/VirtualMouse.git

```
2. Install the required dependencies:
```bash
pip install opencv-python mediapipe autopy

```
## Usage

Run the main script:
```bash
python main.py

```
Ensure your hand is visible to the webcam and use the following gestures:
- Move your index finger to control the cursor
- Bring your index and middle fingers close together to perform a left-click
- Raise all fingers to pause cursor control


## Screenshots
![Screenshot 2024-08-22 231224](https://github.com/user-attachments/assets/ecdcec3f-5211-4ea3-9e3e-2c1824e35b72)
![Screenshot 2024-08-22 231237](https://github.com/user-attachments/assets/04fa3f6a-622a-425e-8a30-5a3c70f7a331)
![Screenshot 2024-08-22 231252](https://github.com/user-attachments/assets/f0d56254-8605-4b82-9d63-adbf951a3c4a)
![Screenshot 2024-08-22 231300](https://github.com/user-attachments/assets/c66b2493-5244-48a4-a5fd-3389588df152)


## Future Improvements

- Implement right-click functionality
- Add drag-and-select capability
- Incorporate keyboard functionalities

## Applications

- Touchless computer control, especially useful in sterile environments
- Accessibility tool for individuals with limited hand mobility
- Interactive displays and presentations
- Virtual and augmented reality interfaces

## Contributing

Contributions to improve the project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push to your fork and submit a pull request

## License

MIT License

## Acknowledgements

- This project was developed under the supervision of Ms. Nida Iftekhar at Jamia Hamdard, New Delhi.
- Thanks to Google's MediaPipe team for their open-source hand tracking solution.

## Contact

Mohammad Zaid - mdzaid786291@gmail.com

Project Link: [https://github.com/yourusername/virtual-cursor-control](https://github.com/diaz3z/VirtualMouse)
