"""Generate inspection checklist from detection results."""
import csv

def save_checklist(checklist, output_path):
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["item", "result"])
        writer.writeheader()
        writer.writerows(checklist)
    print(f"Checklist saved: {output_path}")
