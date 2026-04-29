# SiteWise.AI
## AI-Assisted Visual Inspection for HVAC Duct Installation QA/QC

SiteWise.AI is an AI-assisted visual inspection framework developed for
the Final Master's Project in the MSc in Artificial Intelligence for
Architecture and Construction.

The project focuses on HVAC duct installation QA/QC by using computer
vision to analyse site images, detect ductwork components, compare
observed installation features with reference drawings, and generate
structured inspection checklists.

## Project objective

The objective is to demonstrate the technical feasibility of a
Capture-to-Intelligence workflow:

1. Capture site image during inspection.
2. Detect HVAC duct installation features using YOLO.
3. Refine visual understanding using SAM segmentation.
4. Compare detected features against reference drawings or expected
   configurations.
5. Generate an AI-assisted inspection checklist and annotated output.

## Project scope

The project focuses on visually detectable HVAC duct installation
features:

- Duct count
- Support hangers / threaded rods
- Flexible duct segments
- Installation continuity
- Visible gaps or incomplete connections

The system does not replace professional inspection judgement. It is
designed as a human-in-the-loop decision-support tool.

## AI methods

- **YOLO** — object detection
- **SAM** — segmentation refinement
- **Rule-based checklist logic** — inspection output generation
- **Roboflow** — dataset annotation and management
- **Google Colab** — training and experimentation

## Repository structure

| Folder | Contents |
|--------|----------|
| 00_project_management/ | Meeting notes, mentor feedback, task planning |
| 01_documentation/ | FMP submissions, syllabus, literature review |
| 02_data/ | Raw, processed, annotated, and Roboflow datasets |
| 03_notebooks/ | Google Colab notebooks |
| 04_src/ | Reusable Python scripts |
| 05_models/ | Trained model weights, logs, metrics |
| 06_sample_projects/ | Sample test projects with drawings, images, outputs |
| 07_outputs/ | Generated annotated images, checklists, reports |
| 08_demo/ | Pilot demo video, screenshots, presentation material |
| 09_archive/ | Superseded models, datasets, and documents |

## Pilot demonstration

The pilot demonstration shows:

- Site image input
- YOLO detection of ductwork features
- SAM segmentation refinement
- Feature-based comparison with reference drawings
- Checklist generation
- Annotated inspection output

## Current status

- Problem framing completed
- Data strategy defined
- AI methodology selected
- Pilot workflow under development

## Team

Group 3 — MSc in Artificial Intelligence for Architecture and
Construction

| Name | Role |
|------|------|
| Peace Olaniyi | Wall penetration images, drawings |
| Shaima Husameldin | HVAC duct dataset |
| Rakesh Pandey | HVAC duct dataset |
| Mohammed Musleh | HVAC ductwork dataset |
| Moses Okwiri | Repository setup and management |
