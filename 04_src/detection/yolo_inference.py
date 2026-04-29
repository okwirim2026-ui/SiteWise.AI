"""Run YOLOv8 inference on site images."""
from ultralytics import YOLO

def detect(image_path, model_path="yolov8n.pt", save=True):
    model = YOLO(model_path)
    results = model(image_path, save=save)
    return results
