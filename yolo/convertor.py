from ultralytics import YOLO
import tensorflow as tf

model = YOLO("yolov8n.pt")

# Export model to TensorFlow format
model.export(format="saved_model")
saved_model_dir = "saved_model"
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
tflite_model = converter.convert()

with open("model.tflite", "wb") as f:
    f.write(tflite_model)
