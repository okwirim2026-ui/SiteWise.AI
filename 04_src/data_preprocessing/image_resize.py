"""Resize and prepare images for YOLO training."""
import cv2, os

def resize_image(input_path, output_path, size=(640, 640)):
    img = cv2.imread(input_path)
    resized = cv2.resize(img, size)
    cv2.imwrite(output_path, resized)
    print(f"Saved: {output_path}")
