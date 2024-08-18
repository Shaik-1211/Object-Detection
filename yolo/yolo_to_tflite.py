import torch
import onnx

# Load your YOLO model
model = torch.hub.load('ultralytics/yolov8', 'custom', path='yolov8n.pt')
# Set the model to inference mode
model.eval()

# Input to the model
dummy_input = torch.randn(1, 3, 640, 640)

# Export the model
torch.onnx.export(model, dummy_input, "yolov5s.onnx", verbose=True)
