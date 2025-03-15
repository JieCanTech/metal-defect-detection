#查看数据集是否正确加载，这里我运行的时候已经显示加载正确了，但是类别仍显示COCO预设的，我清理了缓存还是不行，可以直接跳过这个验证，进入yolo训练，
from ultralytics import YOLO

# 读取 dataset.yaml 以确认它是否正确加载
import yaml
with open("E:/visual/NEU-DET/train/dataset.yaml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)
print("Loaded dataset:", data)

# 运行 YOLO 验证
model = YOLO("yolov8n.pt")
model.val(data="E:/visual/NEU-DET/train/dataset.yaml")
