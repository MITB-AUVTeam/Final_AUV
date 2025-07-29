from ultralytics import YOLO

model = YOLO('runs/detect/train/weights/best.pt')

metrics = model.val(
    data='config.yaml',  
    split='test',        
    batch=2,
    conf=0.2,
    iou=0.5,
    plots=True,          
    save_json=True       
)

print(f"Performance on test dataset:")
print(f"mAP50-95: {metrics.box.map:.4f}")
print(f"mAP50: {metrics.box.map50:.4f}")
print(f"Precision: {metrics.box.mp:.4f}")
print(f"Recall: {metrics.box.mr:.4f}")