# Models

This folder stores trained model weights, logs, and metrics.

## YOLOv8

- weights/ — saved .pt checkpoint files
- training_logs/ — run logs from Ultralytics training
- metrics/ — mAP, precision, recall per model version

## SAM

- configs/ — SAM model configuration files
- output_masks/ — saved segmentation mask outputs

## Note on large files

Base model weights (yolov8n.pt, sam_vit_b.pth) are not committed to this repo due to file size.
Download instructions are in 03_notebooks/02_yolo_training_colab.ipynb.
