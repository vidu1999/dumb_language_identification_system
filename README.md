# Deaf and Dumb Language Identification System

## Project Overview
The **Deaf and Dumb Language Identification System** is an innovative solution designed to bridge the communication gap between individuals with hearing and speech impairments and the general public. This system utilizes **computer vision, machine learning, and deep learning** to recognize and interpret sign language gestures in real time, converting them into text or speech output.

## Features
- **Real-Time Gesture Recognition:** Uses advanced image processing techniques to recognize hand signs.
- **Machine Learning Model:** Trained on a diverse dataset for high accuracy.
- **Multilingual Support:** Can be expanded to support multiple sign languages.
- **User-Friendly Interface:** Intuitive design for ease of use.
- **Hardware Integration:** Compatible with cameras and other input devices.

## Technologies Used
- **Programming Languages:** Python
- **Frameworks & Libraries:** TensorFlow, OpenCV, MediaPipe, Keras, NumPy, Pandas
- **Model Type:** Deep Learning-based Hand Gesture Recognition
- **Hardware Requirements:** Webcam, GPU (for model acceleration)

## Installation & Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/dumb-language-identification.git
   ```
2. Navigate to the project directory:
   ```sh
   cd dumb-language-identification
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the application:
   ```sh
   python main.py
   ```

## How It Works
1. The system captures hand gestures using a webcam.
2. The captured frames are processed using **OpenCV** and **MediaPipe** to extract hand landmarks.
3. A **deep learning model** classifies the gestures and converts them into text.
4. The identified text is displayed on-screen or converted into speech using **Text-to-Speech (TTS)** technology.

## Challenges & Solutions
### **Challenge:** Achieving high accuracy in different lighting conditions.
- **Solution:** Implemented data augmentation techniques to improve model generalization.

### **Challenge:** Differentiating similar hand signs.
- **Solution:** Used advanced feature extraction techniques and a well-structured dataset.

## Future Enhancements
- **Mobile Application:** Expanding the system to mobile platforms.
- **Additional Sign Languages:** Supporting ASL, BSL, and other regional sign languages.
- **Voice Integration:** Enabling voice-assisted feedback for users.

## Contribution
We welcome contributions! If you would like to improve the system, feel free to fork the repository and submit a pull request.

## Contact
For any inquiries, feel free to reach out via email at **vidurakavindadev@gmail,com**.

---
### **Developed By:**
**Vidura Kavinda**  
Intern Software Engineer | Machine Learning Enthusiast

