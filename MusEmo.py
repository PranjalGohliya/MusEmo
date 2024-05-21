import cv2
from deepface import DeepFace
import pandas as pd
import tkinter as tk
from tkinter import messagebox

# Music dataset (emotion: [song list])
music_data = {
    'happy': ['Happy Song 1', 'Happy Song 2', 'Happy Song 3'],
    'sad': ['Sad Song 1', 'Sad Song 2', 'Sad Song 3'],
    'angry': ['Angry Song 1', 'Angry Song 2', 'Angry Song 3'],
    'neutral': ['Neutral Song 1', 'Neutral Song 2', 'Neutral Song 3'],
    'surprise': ['Surprise Song 1', 'Surprise Song 2', 'Surprise Song 3'],
    'fear': ['Fear Song 1', 'Fear Song 2', 'Fear Song 3'],
    'disgust': ['Disgust Song 1', 'Disgust Song 2', 'Disgust Song 3']
}

# Function to recommend music based on emotion
def recommend_music(emotion):
    songs = music_data.get(emotion, [])
    if songs:
        return songs[0]  # return the first song for simplicity
    return "No songs available"

# Function to detect emotion
def detect_emotion():
    # Start the webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not ret:
        messagebox.showerror("Error", "Failed to capture image")
        cap.release()
        return
    
    # Analyze the captured frame
    result = DeepFace.analyze(frame, actions=['emotion'])
    cap.release()
    
    # Get the dominant emotion
    emotion = result['dominant_emotion']
    messagebox.showinfo("Emotion Detected", f"Detected Emotion: {emotion}")
    
    # Recommend music based on the detected emotion
    song = recommend_music(emotion)
    messagebox.showinfo("Music Recommendation", f"Recommended Song: {song}")

# GUI setup using Tkinter
root = tk.Tk()
root.title("Music Recommendation System")
root.geometry("400x200")

# Create a button to capture emotion and recommend music
btn = tk.Button(root, text="Capture Emotion and Recommend Music", command=detect_emotion)
btn.pack(pady=50)

root.mainloop()
