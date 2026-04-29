"""SAM segmentation using YOLO bounding boxes as prompts."""
import numpy as np
from segment_anything import sam_model_registry, SamPredictor

def load_sam(checkpoint, model_type="vit_b"):
    sam = sam_model_registry[model_type](checkpoint=checkpoint)
    return SamPredictor(sam)

def segment(predictor, image_rgb, bbox):
    predictor.set_image(image_rgb)
    masks, scores, _ = predictor.predict(box=np.array(bbox)[None, :], multimask_output=False)
    return masks, scores
