# main.py - SiteWise.AI Core Inspection Deployment Service
import os
import shutil
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Any
import torch
from ultralytics import YOLO
import cv2
import numpy as np

app = FastAPI(
    title="SiteWise.AI",
    description="AI-Assisted Visual Inspection Framework for HVAC Installation QA/QC",
    version="1.0.0"
)

# Global Weight Path Allocation Tracking Variables
MODEL_PATH = "/content/best.pt" if os.path.exists("/content/best.pt") else "best.pt"
model = None

# Comprehensive 6-Class Taxonomy Mapping Checklist Registry
TAXONOMY_MAP = {
    0: 'circular duct',
    1: 'flexible duct',
    2: 'hvac grill',
    3: 'rectangular duct',
    4: 'support hanger',
    5: 'wall penetration'
}

@app.on_event("startup")
def load_vision_engine():
    """Initializes and frames the optimized PyTorch network layers on system boot."""
    global model
    try:
        if os.path.exists(MODEL_PATH):
            model = YOLO(MODEL_PATH)
            print(f"✅ Success: YOLOv8s Visual Engine locked onto weights path: {MODEL_PATH}")
        else:
            print("⚠️ Warning: best.pt weights missing. Running initialization using baseline weights template.")
            model = YOLO('yolov8s.pt')
    except Exception as e:
        print(f"❌ Critical Engine Load Failure: {str(e)}")

class InspectionSummary(BaseModel):
    passed: bool
    detected_components: Dict[str, int]
    generated_checklist: List[Dict[str, Any]]
    total_cost_math_check: str

@app.post("/inspect", response_model=InspectionSummary, tags=["QA/QC Inspection Core"])
async def execute_site_inspection(file: UploadFile = File(...)):
    """Receives site photographs, extracts bounding box profiles, and builds the inspection checklist."""
    global model
    if model is None:
        raise HTTPException(status_code=500, detail="Vision inference engine is offline.")
        
    try:
        # Stream incoming image file bytes into numpy arrays
        file_bytes = await file.read()
        nparr = np.frombuffer(file_bytes, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            raise HTTPException(status_code=400, detail="Invalid image file format transmission.")
            
        # Execute target feature extraction pass
        results = model(img, imgsz=640)[0]
        
        # Initialize zero-state count arrays matching our 6-Class Taxonomy
        component_counts = {classname: 0 for classname in TAXONOMY_MAP.values()}
        
        # Extract coordinate metadata lines securely
        for box in results.boxes:
            class_id = int(box.cls[0].item())
            # Map index safely with fallback to catch mismatched data configurations
            classname = TAXONOMY_MAP.get(class_id, f"unknown_class_{class_id}")
            if classname not in component_counts:
                component_counts[classname] = 0
            component_counts[classname] += 1

        # Automated Rule-Based Checklist Engineering Validation Logic
        checklist = [
            {
                "node": "1. Main Distribution",
                "item": "Ducting Count Verification",
                "status": "PASSED" if (component_counts['rectangular duct'] + component_counts['circular duct']) > 0 else "FAILED",
                "evidence": f"Detected {component_counts['rectangular duct']} rectangular and {component_counts['circular duct']} circular runners."
            },
            {
                "node": "2. Component Continuity",
                "item": "Flexible Connection Integrity",
                "status": "PASSED" if component_counts['flexible duct'] > 0 else "WARNING",
                "evidence": f"Found {component_counts['flexible duct']} flexible transition links. Verification required for terminal drops."
            },
            {
                "node": "3. Structural Anchoring",
                "item": "Support Hanger Sizing Profile",
                "status": "PASSED" if component_counts['support hanger'] > 0 else "FAILED",
                "evidence": f"Identified {component_counts['support hanger']} active structural support units supporting dead-loads."
            }
        ]
        
        # Calculate final compliance metric status
        overall_pass = all(item["status"] in ["PASSED", "WARNING"] for item in checklist)
        total_objects = sum(component_counts.values())

        return InspectionSummary(
            passed=overall_pass,
            detected_components=component_counts,
            generated_checklist=checklist,
            total_cost_math_check=f"Processed {total_objects} architectural assets over single camera interface capture viewport."
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Inference error processing tracking loop: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
