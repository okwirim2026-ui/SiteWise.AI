"""YOLOv8 training script for HVAC duct detection."""
from ultralytics import YOLO

def train(data_yaml, epochs=50, imgsz=640):
    model = YOLO("yolov8n.pt")
    results = model.train(data=data_yaml, epochs=epochs, imgsz=imgsz)
    return results
