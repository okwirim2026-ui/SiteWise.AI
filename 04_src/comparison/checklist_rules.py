"""Rule-based logic for generating inspection checklist items."""

DETECTION_CLASSES = [
    "rectangular_duct",
    "flexible_duct",
    "support_hanger",
    "duct_joint",
    "visible_gap"
]

def evaluate_detections(detections):
    checklist = []
    classes_found = [d["class"] for d in detections]
    checklist.append({"item": "Rectangular ducts detected", "result": "rectangular_duct" in classes_found})
    checklist.append({"item": "Support hangers present", "result": "support_hanger" in classes_found})
    checklist.append({"item": "Visible gaps flagged", "result": "visible_gap" in classes_found})
    return checklist
