# Data

This folder contains all image datasets, annotations, and processed data for SiteWise.AI.

## Folder structure

- raw/ — original source images
  - site_images/ — real site photographs
  - drawing_snapshots/ — cropped 2D drawing references
  - reference_images/ — additional HVAC reference material
- roboflow_exports/ — dataset versions exported from Roboflow
- processed/ — train/valid/test split datasets
- annotations/ — YOLO labels, COCO annotations, class mapping

## Dataset classes

| ID | Class | Description |
|----|-------|-------------|
| 0 | rectangular_duct | Rigid metal duct section |
| 1 | flexible_duct | Flexible duct segment |
| 2 | support_hanger | Support hanger or threaded rod |
| 3 | duct_joint | Duct joint or connection point |
| 4 | visible_gap | Visible gap or discontinuity |

## Contributors

| Contributor | Images | Folder |
|-------------|--------|--------|
| Shaima Husameldin | 175 | site_images/ |
| Mohammed Musleh | 100 | site_images/ |
| Peace Olaniyi | 54 | site_images/ |

## Data governance

No confidential or personally identifiable information is stored here.
All site images have been reviewed for anonymisation compliance.
