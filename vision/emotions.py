import cv2
import numpy as np
from fer import FER
import matplotlib.pyplot as plt

def detect_emotions(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert the image to RGB (OpenCV loads images in BGR format by default)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Initialize the FER model
    emotion_detector = FER()
    
    # Detect emotions
    emotions = emotion_detector.detect_emotions(image_rgb)
    
    emotion_detected = ''
    # Draw bounding boxes and emotion labels on the image
    for result in emotions:
        bounding_box = result['box']
        emotions = result['emotions']
        
        # Get the dominant emotion
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Draw the bounding box
        x, y, w, h = bounding_box
        cv2.rectangle(image_rgb, (x, y), (x + w, y + h), (0, 255, 0), 2)
        emotion_detected = dominant_emotion
        # Put the emotion label
        cv2.putText(image_rgb, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    
    # Display the result
    plt.imshow(image_rgb)
    plt.axis('off')
    # plt.show()
    return emotion_detected
