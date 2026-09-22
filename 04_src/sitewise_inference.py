#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# ==============================================================================
# 📊 EMBEDDED RESEARCH METRICS & DATA-SCIENCE PROFILE LEDGER
# ==============================================================================
RESEARCH_METRICS = {
    "Project Name": "SiteWise_Final_Master_Pool",
    "Framework Model Layer": "YOLOv8s (Ultralytics PyTorch Core Core)",
    "Training Input Split Source": "29 High-Fidelity Generative Gemini Synthetic Variations",
    "Validation Pass Target Pool": "81 Real-World On-Site Construction Photographs",
    "Optimization Metric Results": {
        "Model General Precision": "23.30%",
        "Mean Average Precision (mAP50)": "4.37%",
        "Spatial Bounding Box Fitness (mAP50-95)": "2.02%",
        "General Model Recall Rate": "6.21%"
    },
    "Annotated Training Distribution Matrix": {
        "flexible duct": 22,
        "rectangular duct": 16,
        "support hanger": 15,
        "hvac grill": 11,
        "circular duct": 6,
        "wall penetration": 0
    }
}

def print_academic_summary():
    print("=" * 70)
    print(f"🚀 SITEWISE.AI - INFERENCE ENGINE & METRICS LEDGER VERSION 1.0")
    print("=" * 70)
    for key, val in RESEARCH_METRICS.items():
        if isinstance(val, dict):
            print(f"\n📈 {key.upper()}:")
            for sub_k, sub_v in val.items():
                print(f"  ├── {sub_k:<42} : {sub_v}")
        else:
            print(f"🔹 {key:<30} : {val}")
    print("=" * 70)
    print("\n[INFO] Initializing convolutional framework runtime dependencies...")

# ==============================================================================
# ⚙️ LIVE OBJECT DETECTION INFERENCE RUNTIME PIPELINE LAYER
# ==============================================================================
def run_live_inference(image_filename="target_ceiling_photo.jpg", model_weights="best.pt"):
    current_dir = Path(__file__).parent.resolve()
    model_path = current_dir / model_weights
    image_path = current_dir / image_filename
    output_dir = current_dir / "evaluation_results"

    if not model_path.exists():
        print(f"\n❌ RUNTIME ERROR: Model weights file '{model_weights}' could not be located.")
        print(f"Please copy your downloaded 'best.pt' file into this directory path:\n➔ {current_dir}\n")
        sys.exit(1)

    if not image_path.exists():
        print(f"\n⚠️ INPUT WARNING: Target photograph '{image_filename}' not found.")
        print(f"Please drop a test image into the directory and name it '{image_filename}' to execute a live scan.")
        print("\n[IDLE] Script tracking data output completed successfully.")
        sys.exit(0)

    try:
        from ultralytics import YOLO
    except ImportError:
        print("\n⏳ DEPENDENCY NOTICE: Installing required Ultralytics framework libraries...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "ultralytics"])
        from ultralytics import YOLO

    print(f"\n🎬 Activating custom model: {model_weights}")
    print(f"🎯 Scanning target image scene properties: {image_filename}")
    
    model = YOLO(str(model_path))
    results = model.predict(source=str(image_path), imgsz=640, conf=0.25, save=False)

    os.makedirs(output_dir, exist_ok=True)
    annotated_frame = results.plot()
    
    import cv2
    output_path = output_dir / f"annotated_{image_path.stem}.jpg"
    cv2.imwrite(str(output_path), annotated_frame)
    
    print("\n" + "🎉" * 20)
    print(f"✅ DETECTIONS COMPLETED SUCCESSFULLY!")
    print(f"➔ Output annotated visual box layers saved at: {output_path.resolve()}")
    print("🎉" * 20 + "\n")

if __name__ == "__main__":
    print_academic_summary()
    run_live_inference(image_filename="target_ceiling_photo.jpg", model_weights="best.pt")
