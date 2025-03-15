#查看数据集是否正确加载
from ultralytics import YOLO

# 读取 dataset.yaml 以确认它是否正确加载
import yaml
with open("E:/visual/NEU-DET/train/dataset.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
print("Loaded dataset:", data)

# 运行 YOLO 验证
model = YOLO("yolov8n.pt")
model.val(data="E:/visual/NEU-DET/train/dataset.yaml")
