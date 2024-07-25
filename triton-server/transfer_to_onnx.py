from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.pt")  # load an official model

# Export the model
onnx_file = model.export(format="onnx", dynamic=True)