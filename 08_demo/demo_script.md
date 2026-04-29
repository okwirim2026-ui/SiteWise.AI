# Pilot demo script

## Overview

This script outlines the steps for the SiteWise.AI pilot demonstration.

## Steps

1. Open 04_inference_and_checklist_demo.ipynb in Google Colab
2. Load the 3 pilot images from 02_data/raw/site_images/
3. Run YOLOv8 detection — show bounding box output
4. Run SAM segmentation — show mask overlay
5. Show generated inspection checklist
6. Compare with drawing snapshot
7. Present annotated output for inspector review

## Talking points

- System is decision-support, not automated certification
- Human verification is mandatory
- Target performance: mAP 80–90%
- Pipeline: Capture → Detect → Segment → Compare → Checklist → Review
